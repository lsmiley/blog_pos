from django.test import TestCase
from django.urls import reverse

class sizingorderDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_sizingorder_detail_page(self):
        response = self.client.get(reverse('sizingorder_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sizingorder/sizingorder_detail.html')