from django.urls import resolve
from django.test import TestCase
from django.test import Client
from django.http import HttpRequest
from .models import Post
from .views import *


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_home_page_returns_correct_html(self):
        #request = HttpRequest()
        #response = post_list(request)
        c = Client()
        response = c.get('')
        #print('это респонсе!!!', response, response.status_code, response.content)
        html = response.content.decode('utf8')
        #print('А ЭТО стартсвис: ',html.startswith)
        self.assertTrue(html.startswith('\n<!DOCTYPE '))
        self.assertIn('<title>ТОНАЛЬ</title>', html)
        self.assertIn('<h1>ЗАЩИТНЫЕ ПОКРЫТИЯ ТОНАЛЬ</h1>', html)
        self.assertTrue(html.endswith('</html>'))
