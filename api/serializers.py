from rest_framework import serializers
from .models import *

class PersonalCreditSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name')
    class Meta:
        model = PersonalCredit
        fields = ('id', 'amount', 'approvement', 'client', 'client_name')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'SBS_debt', 'sentinel_score', 'ai_algorithm',)

class PersonalCreditUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalCredit
        fields = ('approvement',)