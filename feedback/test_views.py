from django.test import TestCase
from .models import Feedback
from profiles.models import UserProfile


class TestViews(TestCase):

    def test_get_feedback_page(self):
        response = self.client.get('/feedback/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback/feedback.html')
    """
    def test_get_add_feedback_page(self):
        response = self.client.get('/feedback/add/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback/add_feedback.html')
    """
    """
    def test_get_edit_feedback_page(self):
        user = UserProfile.objects.create({user.id})
        feedback = Feedback.objects.create(full_name='Test Name', email='test@test.com', feedback='test feedback')
        response = self.client.get(f'/feedback/edit/{feedback.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback/edit_feedback.html')
    """
    def test_can_add_feedback(self):
        response = self.client.post('/feedback/add/', {'full_name': 'Test Name', 'email': 'test@test.com', 'feedback': 'test feedback'})
        self.assertRedirects(response, '/accounts/login/?next=/feedback/add/')
    """
    def test_can_delete_feedback(self):
        feedback = Feedback.objects.create(full_name='Test Name', email='test@test.com', feedback='test feedback')
        response = self.client.get(f'/feedback/delete/{feedback.id}')
        self.assertRedirects(response, '/feedback/')
        existing_feedback = Feedback.objects.filter(id=feedback.id)
        self.assertEqual(len(existing_feedback), 0)
    """
