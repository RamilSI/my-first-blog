from datetime import datetime

from django.urls import resolve
from django.test import TestCase
from django.test import Client
from django.http import HttpRequest
from blog.models import Post
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


class PostModelTest(TestCase):
    def test_post_open_and_save(self):
        # создай статью 1
        # сохрани статью 1 в базе
        post1 = Post(
            title='post 1',
            text='full_text 1',
            summary='summary 1',
            category = 'category1',
            created_date=datetime.now())
        post1.save()

        # создай статью 2
        # сохрани статью 2 в базе
        post2 = Post(
            title='post 2',
            text='full_text 2',
            summary='summary 2',
            category='category2',
            created_date=datetime.now())
        post2.save()

        # загрузи из базы все статьи
        all_post = Post.objects.all()
        # статей должно быть две
        self.assertEqual(len(all_post),2)
        # проверь: 1 загруженная статья == статья 1
        self.assertEqual(
            all_post[0].title,
            post1.title)
        # проверь: 2 загруженная статья == статья 2
        self.assertEqual(
            all_post[1].title,
            post2.title)

# есть новые статьи в админке, но они могут быть не опубликованы