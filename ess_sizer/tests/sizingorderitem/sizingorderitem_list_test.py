from django.test import TestCase
from django.urls import reverse

class sizingorderitemListTestCase(TestCase):
    def setUp(self):
        pass

    def test_sizingorderitem_list_page(self):
        response = self.client.get(reverse('sizingorderitem_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sizingorderitem/sizingorderitem_list.html')