from django.test import TestCase


class TestViews(TestCase):
    # Test to check correct template is used
    def test_get_weapons_page(self):
        response = self.client.get('/weapons/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'weapons/weapons.html')

    # Test to check login required to add a review
    def test_login_required_to_add_review(self):
        response = self.client.post('/weapons/add/', {'weapon': 'test', 'full_name': 'Test Name', 'email': 'test@test.com', 'feedback': 'test feedback'})
        self.assertRedirects(response, '/accounts/login/?next=/weapons/add/')
