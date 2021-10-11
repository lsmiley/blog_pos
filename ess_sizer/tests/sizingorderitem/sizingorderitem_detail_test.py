from django.test import TestCase
from django.urls import reverse

class sizingorderitemDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_sizingorderitem_detail_page(self):
        response = self.client.get(reverse('sizingorderitem_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sizingorderitem/sizingorderitem_detail.html')