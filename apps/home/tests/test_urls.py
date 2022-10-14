from django.test import TestCase
from django.urls import reverse


class HomeURLsTest(TestCase):
    def test_url_home_ok(self):
        home_url = reverse('home:home')
        self.assertEqual(home_url, '/')
