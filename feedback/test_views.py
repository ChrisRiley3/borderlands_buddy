from django.test import TestCase


class TestViews(TestCase):
    # Tests to see if the correct template is used
    def test_get_feedback_page(self):
        response = self.client.get('/feedback/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback/feedback.html')

    # Tests to see if the user is logged in to add feedback
    def test_required_login_to_add_feedback(self):
        response = self.client.post('/feedback/add/', {'full_name': 'Test Name', 'email': 'test@test.com', 'feedback': 'test feedback'})
        self.assertRedirects(response, '/accounts/login/?next=/feedback/add/')
