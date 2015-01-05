# coding: utf-8
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class GraphTest(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create(
            username='admin', password='admin',
            is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('admin')
        self.user.save()
        self.login = self.c.login(username='admin', password='admin')
        self.resp = self.c.get('/admin/graph-of-pets/')

    def test_get(self):
        """
        GET / must return status code 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/graph.html')
