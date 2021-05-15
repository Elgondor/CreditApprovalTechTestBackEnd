from rest_framework import serializers
from .models import *

class PersonalCreditSerializer(serializers.ModelSerializer):
    # client_name = serializers.CharField(source='client.name')
    class Meta:
        model = PersonalCredit
        fields = ('id', 'amount', 'approvement', 'client', 'ai_algorithm',)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'SBS_debt', 'client_score', 'sentinel_score')



class PersonalCreditUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalCredit
        fields = ('approvement',)