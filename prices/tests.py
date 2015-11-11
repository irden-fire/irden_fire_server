# coding=utf8
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Price

def create_price(name, cost, duration, how_many_participants, description):
    """
    Create a price objects with filled fields
    """
    return Price.objects.create(name=name, cost=cost, duration=duration,
                                    how_many_participants=how_many_participants,
                                    description=description)

class PriceMethodTests(TestCase):

    def test_price_was_created(self):
        """
        Check that cyrrylic symbols are properly saves to database
        """
        created_price = create_price( 'тестовый прайс', 0.99, '5', '1', 'simple description')
        self.assertEqual(created_price.name, 'тестовый прайс')

    def test_price_not_found(self):
        """
        Check that if price id doesn't exist, 404 page are raising
        """
        created_price = create_price( 'test price', 0.99, '5', '1', 'simple description')
        response = self.client.get('/prices/4/')
        self.assertEqual(response.status_code, 404)

    def test_price_found(self):
        """
        Check that if price id exist, response contains proper record name and
        response code is 200
        """
        created_price = create_price( 'test price', 0.99, '5', '1', 'simple description')
        response = self.client.get('/prices/1/')
        self.assertContains(response, created_price.name,
                            status_code=200)
