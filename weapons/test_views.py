from django.test import TestCase


class TestViews(TestCase):

    def test_weapons_page(self):
        response = self.client.get('/weapons/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weapons/weapons.html')


