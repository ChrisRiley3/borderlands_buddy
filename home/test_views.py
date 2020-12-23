from django.test import TestCase


class TestViews(TestCase):
    # Tests to see if the correct template is used
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
