from django.db import models
import random

class Client(models.Model):
    class Score(models.IntegerChoices):
        BAD = 1
        REGULAR = 2
        GOOD = 3

    SBS_debt = models.IntegerField()
    client_score = models.IntegerField(choices = Score.choices)
    sentinel_score = models.IntegerField()

    @staticmethod
    def name(self):
        return 'henry'


class PersonalCredit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.IntegerField()
    approvement = models.BooleanField(default=False)

    @staticmethod
    def ai_algorithm():
        return random.randrange(1, 10)
    
    

