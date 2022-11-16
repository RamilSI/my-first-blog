import unittest
from django.test import TestCase
from models import *

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 2, 3)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(False, False)  # add assertion here

class TestModelPost(TestCase):
    post = Post.get


if __name__ == '__main__':
    unittest.main()
