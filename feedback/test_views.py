from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.feedback_url = reverse('feedback')

    def test_get_feedback_page(self):
        response = self.client.get(self.feedback_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback/feedback.html')
