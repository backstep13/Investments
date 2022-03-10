from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from button.models import Investment
from button.serializers import InvestmentSerializer


class InvestmentApiTestCase(APITestCase):
    def setUp(self):
        """Create user and items of investment for tests"""
        self.user = User.objects.create(username='usr', password='secret')
        self.invest_1 = Investment.objects.create(investor=self.user, interval=12, amount=500, percent=10)
        self.invest_2 = Investment.objects.create(investor=self.user, interval=10, amount=100, percent=7)

    def test_get(self):
        """Test get-method API,
        receive list of investments for authorized user"""
        url = reverse('investments-list')  # or inv-detail
        self.client.force_login(self.user)  # log-in
        response = self.client.get(url)
        serializer_data = InvestmentSerializer([self.invest_1, self.invest_2], many=True).data  # if not list many=False
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_not_auth(self):
        """Test get-method API, if user not authorized
        receive error 403"""
        url = reverse('investments-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_get_search(self):
        """Test how work search in GET request"""
        url = reverse('investments-list')
        self.client.force_login(self.user)
        response = self.client.get(url, data={'search': 10})  # data -> ?search=10
        serializer_data = InvestmentSerializer([self.invest_1, self.invest_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
