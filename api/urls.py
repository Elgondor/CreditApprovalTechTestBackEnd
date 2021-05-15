from django.urls import path
from .views import *

urlpatterns = [
    path('credit_approval/<int:pk>', UpdatePersonalCreditAPIView.as_view()),
    path('credits/', ListPersonalCreditAPIView.as_view()),
    path('get_client_profile/<int:pk>', ClientAPIView.as_view()),
]
