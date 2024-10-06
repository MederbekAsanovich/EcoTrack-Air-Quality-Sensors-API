from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Sensor

class SensorTests(APITestCase):
    def test_create_sensor(self):
        url = reverse('sensor-list')
        data = {'type': 'AQ', 'model': 'AQ-100', 'installation_date': '2024-10-06'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
