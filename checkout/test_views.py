from django.test import TestCase


class TestViews(TestCase):

    def test_get_checkout_page(self):
        response = self.client.get('/checkout/')
        self.assertEquals(response.status_code, 302)
