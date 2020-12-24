from django.test import TestCase
from .forms import FeedbackForm


class TestFeedbackForm(TestCase):
    # Test to check customer name is required
    def test_customer_name_is_required(self):
        form = FeedbackForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0], 'This field is required.')

    # Test to check email is required
    def test_email_is_required(self):
        form = FeedbackForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    # Test to check feedback is required
    def test_feedback_is_required(self):
        form = FeedbackForm({'feedback': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('feedback', form.errors.keys())
        self.assertEqual(form.errors['feedback'][0], 'This field is required.')
