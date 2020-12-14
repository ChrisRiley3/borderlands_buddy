from django.test import TestCase


class TestViews(TestCase):

    def test_get_feedback_page(self):
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback/feedback.html')

