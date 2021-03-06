from django.urls import resolve, reverse
from django.test import TestCase
from .views import home


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)


class APITests(TestCase):
    def test_api_status_code(self):
        url = 'https://api.vatcomply.com/rates?base=USD'
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
