from django.test import TestCase


class TestViews(TestCase):

    def test_weapons_page(self):
        response = self.client.get('/weapons/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weapons/weapons.html')

    def test_can_add_review(self):
        response = self.client.post('/weapons/add/', {'weapon': 'test', 'full_name': 'Test Name', 'email': 'test@test.com', 'feedback': 'test feedback'})
        self.assertRedirects(response, '/accounts/login/?next=/weapons/add/')
