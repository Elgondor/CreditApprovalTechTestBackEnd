from rest_framework import generics
from .models import *
from .serializers import PersonalCreditSerializer, ClientSerializer, PersonalCreditUpdateSerializer


class ListPersonalCreditAPIView(generics.ListAPIView):
    queryset = PersonalCredit.objects.filter(amount__lte=50000)
    serializer_class = PersonalCreditSerializer

    # def get_queryset(self):
    #     queryset = PersonalCredit.objects.all()
    #     amount_query = self.request.query_params.get('tags', None)


class UpdatePersonalCreditAPIView(generics.UpdateAPIView):
    queryset = PersonalCredit.objects.all()
    serializer_class = PersonalCreditUpdateSerializer



class ClientAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


    