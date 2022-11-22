import unittest
from django.test import TestCase
from .models import *
from django.urls import resolve
from .views import *

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        print(f'поиск функции - {found.func}')
        self.assertEqual(found.func, post_list)

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 2, 3)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(False, False)  # add assertion here

class TestModelPost(TestCase):
    post = Post.objects.get()
    print(post)


if __name__ == '__main__':
    unittest.main()
