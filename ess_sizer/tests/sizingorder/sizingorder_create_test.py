from django.test import TestCase
from django.urls import reverse

class sizingorderCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_sizingorder_create_page(self):
        response = self.client.get(reverse('sizingorder_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sizingorder/sizingorder_create.html')