from django.test import TestCase
from .models import Feedback
from profiles.models import UserProfile


class TestViews(TestCase):

    def test_get_feedback_page(self):
        response = self.client.get('/feedback/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback/feedback.html')

    def test_can_add_feedback(self):
        response = self.client.post('/feedback/add/', {'full_name': 'Test Name', 'email': 'test@test.com', 'feedback': 'test feedback'})
        self.assertRedirects(response, '/accounts/login/?next=/feedback/add/')
