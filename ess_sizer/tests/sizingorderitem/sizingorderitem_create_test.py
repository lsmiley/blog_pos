from django.test import TestCase
from django.urls import reverse

class sizingorderitemCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_sizingorderitem_create_page(self):
        response = self.client.get(reverse('sizingorderitem_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sizingorderitem/sizingorderitem_create.html')