from rest_framework import generics
from .models import *
from .serializers import PersonalCreditSerializer, ClientSerializer, PersonalCreditUpdateSerializer


class ListPersonalCreditAPIView(generics.ListAPIView):
    queryset = PersonalCredit.objects.filter(amount__lte=50000)
    serializer_class = PersonalCreditSerializer


class UpdatePersonalCreditAPIView(generics.UpdateAPIView):
    queryset = PersonalCredit.objects.all()
    serializer_class = PersonalCreditUpdateSerializer



class ClientAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


    