from django.test import TestCase
from django.contrib.auth.models import User

from button.models import Investment
from button.serializers import InvestmentSerializer


class InvestmentSerializerTestCase(TestCase):
    def test_ok(self):
        """Chek if we get right data from DB with serializer"""
        user = User.objects.create(username='usr')
        invest_1 = Investment.objects.create(investor=user, interval=12, amount=500, percent=10)
        invest_2 = Investment.objects.create(investor=user, interval=12, amount=100, percent=7)
        data = InvestmentSerializer([invest_1, invest_2], many=True).data
        expected_data = [
            {
                'id': invest_1.id,
                'investor': user.id,
                'i_type': 'deposit',
                'interval': 12,
                'amount': 500,
                'percent': '10.0',
                'back': 0,
                'status': True
            },
            {
                'id': invest_2.id,
                'investor': user.id,
                'i_type': 'deposit',
                'interval': 12,
                'amount': 100,
                'percent': '7.0',
                'back': 0,
                'status': True
            }
        ]
        self.assertEqual(expected_data, data)
