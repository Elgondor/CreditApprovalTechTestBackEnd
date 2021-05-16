from django.db import models
import random

class Client(models.Model):
    class Score(models.IntegerChoices):
        BAD = 1
        REGULAR = 2
        GOOD = 3

    name = models.CharField(max_length=200, null=True)
    SBS_debt = models.IntegerField()
    sentinel_score = models.IntegerField(choices = Score.choices)

    @staticmethod
    def ai_algorithm():
        return random.randrange(1, 10)


class PersonalCredit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.IntegerField()
    approvement = models.BooleanField(default=False)