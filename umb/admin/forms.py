

from umb.admin.models import Weight
from django import forms

class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = '__all__'
