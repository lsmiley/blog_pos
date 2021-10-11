from django.test import TestCase
from django.urls import reverse

class sizingorderDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_sizingorder_delete_page(self):
        response = self.client.get(reverse('sizingorder_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sizingorder/sizingorder_delete.html')