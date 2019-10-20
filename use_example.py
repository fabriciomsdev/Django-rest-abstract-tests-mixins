from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from .tests import *

# Create your tests here.
class SocialPostsTest(
        TestResourceRouteExist,
        TestUserNotLoggedCanNotPost,
        TestUserLoggedCanPost,
        TestUserLoggedCanUpdate,
        TestUserLoggedCanDelete,
        TestCase):

    data_for_test = {
        'title': 'It is a test'
    }
    data_updated_for_test = {
        'title': 'It is a test 2'
    }
    url = '/api/posts/'
