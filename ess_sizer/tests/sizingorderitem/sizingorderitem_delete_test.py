from django.test import TestCase
from django.urls import reverse

class sizingorderitemDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_sizingorderitem_delete_page(self):
        response = self.client.get(reverse('sizingorderitem_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sizingorderitem/sizingorderitem_delete.html')