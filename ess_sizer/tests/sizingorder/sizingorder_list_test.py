from django.test import TestCase
from django.urls import reverse

class sizingorderListTestCase(TestCase):
    def setUp(self):
        pass

    def test_sizingorder_list_page(self):
        response = self.client.get(reverse('sizingorder_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sizingorder/sizingorder_list.html')