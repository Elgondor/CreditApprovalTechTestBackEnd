from django.urls import path
from .views import *

urlpatterns = [
    path('credit_approval/<int:pk>', UpdatePersonalCreditAPIView.as_view(), name = 'credit_approval'),
    path('credits/', ListPersonalCreditAPIView.as_view(), name = 'credits'),
    path('get_client_profile/<int:pk>', ClientAPIView.as_view(), name = 'get_client_profile'),
]
