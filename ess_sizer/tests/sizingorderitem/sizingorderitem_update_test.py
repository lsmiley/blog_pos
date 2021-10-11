from django.test import TestCase
from django.urls import reverse

class sizingorderitemUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_sizingorderitem_update_page(self):
        response = self.client.get(reverse('sizingorderitem_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sizingorderitem/sizingorderitem_update.html')