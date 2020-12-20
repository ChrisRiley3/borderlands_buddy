from django.test import TestCase


class TestViews(TestCase):
    # Tests login required for profiles page
    def test_login_required_to_view_profile(self):
        response = self.client.get('/profile/')
        self.assertRedirects(response, '/accounts/login/?next=/profile/')

    # Tests correct status code for profiles page
    def test_status_code_302_for_profiles(self):
        response = self.client.get('/profile/')
        self.assertEquals(response.status_code, 302)
