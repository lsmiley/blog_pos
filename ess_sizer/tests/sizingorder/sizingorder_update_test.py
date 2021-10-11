from django.test import TestCase
from django.urls import reverse

class sizingorderUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_sizingorder_update_page(self):
        response = self.client.get(reverse('sizingorder_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sizingorder/sizingorder_update.html')