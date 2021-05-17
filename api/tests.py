from django.test import TestCase
from .models import *
from .serializers import *
from django.urls import reverse

class ClientTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_client_one = Client.objects.create(
            name = 'Jhimy Brandon Vallejos Silva',
            SBS_debt = 12345,
            sentinel_score = 1
        )

        test_client_two = Client.objects.create(
            name = '123124erwqersdfcvbqaedwqer poqwkeopqkwepo aspdpoqwkepokaskdxclkv qopwekpqowekpoqwe',
            SBS_debt = 12345345.213,
            sentinel_score = 2
        )

        test_client_three = Client.objects.create(
            name = 'Марія Олександра Родрігес Волошина',
            SBS_debt = 187945632,
            sentinel_score = 3
        )

    def test_client_content(self):
        client_one = Client.objects.get(id=1)
        self.assertEqual(client_one.name, 'Jhimy Brandon Vallejos Silva')
        self.assertEqual(client_one.SBS_debt, 12345)
        self.assertEqual(client_one.sentinel_score, 1)

        client_two = Client.objects.get(id=2)
        self.assertEqual(client_two.name, '123124erwqersdfcvbqaedwqer poqwkeopqkwepo aspdpoqwkepokaskdxclkv qopwekpqowekpoqwe')
        self.assertEqual(client_two.SBS_debt, 12345345)
        self.assertEqual(client_two.sentinel_score, 2)

        client_three = Client.objects.get(id=3)
        self.assertEqual(client_three.name, 'Марія Олександра Родрігес Волошина')
        self.assertEqual(client_three.SBS_debt, 187945632)
        self.assertEqual(client_three.sentinel_score, 3)

    def test_get_client_profile(self):
        response = self.client.get(reverse('get_client_profile', kwargs={'pk': 1}))

        client_one = Client.objects.get(id = 1)
        serializer = ClientSerializer(client_one)
        self.assertNotEqual(response.data, serializer.data)
    


class PersonalCreditTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_client_one = Client.objects.create(
            name = 'Jhimy Brandon Vallejos Silva',
            SBS_debt = 12345,
            sentinel_score = 1
        )

        test_personal_credit_one = PersonalCredit.objects.create(
            client = test_client_one,
            amount = 12345,
            approvement = False
        )

        test_personal_credit_two = PersonalCredit.objects.create(
            client = test_client_one,
            amount = 4800,
            approvement = False
        )

        
    
    def test_get_all_personal_credits(self):
        response = self.client.get(reverse('credits'))

        personal_credits = PersonalCredit.objects.all()
        serializer = PersonalCreditSerializer(personal_credits, many=True)
        self.assertEqual(response.data, serializer.data)





