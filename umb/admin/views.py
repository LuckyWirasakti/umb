from django.core import serializers
from django.views.generic.edit import CreateView
from umb.admin.forms import MasterForm, WeightForm
from umb.admin.models import Master, Weight
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.urls.base import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.views.generic import View
from django.db.models import Avg, Count, Min, Sum

class LoginFormSet(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

class PasswordChangeFormSet(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

class LoginViewSet(LoginView):
    form_class = LoginFormSet
    redirect_authenticated_user = True
    template_name = 'auth/login.html'
    
class LogoutViewset(LogoutView):
    pass
    
    
class BuyViewSet(LoginRequiredMixin, ListView):
    model = Weight
    paginate_by = 15
    template_name = 'buy.html'

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        qs = super().get_queryset()
        if q is not None:
            return qs.filter(name__icontains=q)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amount_weight'] = sum(self.get_queryset().values_list('amount_weight', flat=True))
        context['amount_price'] = sum(self.get_queryset().values_list('amount_price', flat=True))
        return context

class WeightViewSet(LoginRequiredMixin, ListView):
    model = Weight
    paginate_by = 5
    template_name = 'weight.html'

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        qs = super().get_queryset()
        if q is not None:
            return qs.filter(name__icontains=q)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alert'] = Master.objects.filter(key='alert')
        context['discount'] = Master.objects.filter(key='discount')
        context['price'] = Master.objects.filter(key='price')
        return context

class ChangePasswordViewSet(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeFormSet
    template_name = 'change-password.html'
    success_url = reverse_lazy('admin-login')

class CreateWeightViewSet(View):
    def post(self, request):
        if request.is_ajax() and request.method == 'POST':
            form = WeightForm(request.POST)
            if form.is_valid():
                instance = form.save()
                ser_instance = serializers.serialize('json', [ instance, ])
                return JsonResponse({"instance": ser_instance}, status=200)
            else:
                return JsonResponse({"error": form.errors}, status=422)
        return JsonResponse({"error": ""}, status=400)

class UpdateWeightViewSet(View):
    def get(self, request):
        if request.is_ajax() and request.method == 'GET':
            instance = Weight.objects.get(id=request.GET.get('id', None))
            if instance:
                ser_instance = serializers.serialize('json', [ instance, ])
                return JsonResponse({"instance": ser_instance}, safe=True, status=200)
            return JsonResponse({"error": "not found"}, status=404)
        return JsonResponse({"error": ""}, status=400)

    def post(self, request):
        if request.is_ajax() and request.method == 'POST':
            instance = Weight.objects.get(id=request.POST.get('id'))
            if instance is not None:
                form = WeightForm(request.POST, instance=instance)
                if form.is_valid():
                    instance = form.save()
                    ser_instance = serializers.serialize('json', [ instance, ])
                    return JsonResponse({"instance": ser_instance}, status=200)
                else:
                    return JsonResponse({"error": form.errors}, status=422)
            return JsonResponse({"error": "not found"}, status=404)
        return JsonResponse({"error": ""}, status=400)
            

class DeleteWeightViewSet(View):
    def get(self, request):
        if request.is_ajax() and request.method == 'GET':
            delete = request.GET.get('id', None)
            if delete is not None:
                Weight.objects.get(id=delete).delete()
                return JsonResponse({},status=204)
            return JsonResponse({},status=404)
        return JsonResponse({},status=400)

class PrintViewset(ListView):
    model = Weight
    template_name = 'print.html'

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        qs = super().get_queryset()
        if q is not None:
            return qs.filter(name__icontains=q)
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amount_weight'] = sum(self.get_queryset().values_list('amount_weight', flat=True))
        context['amount_price'] = sum(self.get_queryset().values_list('amount_price', flat=True))
        return context

class PrintMobileViewset(DetailView):
    model = Weight
    template_name = 'print-mobile.html'


class MasterViewSet(CreateView):
    form_class = MasterForm
    template_name = 'master.html'
    success_url = reverse_lazy('admin-weight')
