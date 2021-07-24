from umb.admin.views import BuyViewSet, ChangePasswordViewSet, CreateWeightViewSet, DeleteWeightViewSet, LoginViewSet, LogoutViewset, MasterViewSet, PrintMobileViewset, PrintViewset, UpdateWeightViewSet, WeightViewSet
from django.urls import path

urlpatterns = [
    path('', LoginViewSet.as_view(), name='admin-login'),
    path('logout', LogoutViewset.as_view(), name='admin-logout'),
    path('weight', WeightViewSet.as_view(), name='admin-weight'),
    path('master', MasterViewSet.as_view(), name='admin-master'),
    path('weight/create', CreateWeightViewSet.as_view(), name='admin-weight-create'),
    path('weight/update', UpdateWeightViewSet.as_view(), name='admin-weight-update'),
    path('weight/delete', DeleteWeightViewSet.as_view(), name='admin-weight-delete'),
    path('buy', BuyViewSet.as_view(), name='admin-buy'),
    path('print', PrintViewset.as_view(), name='admin-print'),
    path('print/mobile/<int:pk>', PrintMobileViewset.as_view(), name='admin-print-mobile'),
    path('change-password', ChangePasswordViewSet.as_view(), name='admin-change-password'),
]
