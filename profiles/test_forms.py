from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):
    # Test to check default phone number is not required
    def test_default_phone_number_is_not_required(self):
        form = UserProfileForm({'default_phone_number': ''})
        self.assertTrue(form.is_valid())

    # test to check default street address 1 is not required
    def test_default_street_address1_is_not_required(self):
        form = UserProfileForm({'default_street_address1': ''})
        self.assertTrue(form.is_valid())

    # Test to check default street address 2 is not required
    def test_default_street_address2_is_not_required(self):
        form = UserProfileForm({'default_street_address2': ''})
        self.assertTrue(form.is_valid())

    # Test to check default town or city is not required
    def test_default_town_or_city_is_not_required(self):
        form = UserProfileForm({'default_town_or_city': ''})
        self.assertTrue(form.is_valid())

    # Test to check default county is not required
    def test_default_county_is_not_required(self):
        form = UserProfileForm({'default_county': ''})
        self.assertTrue(form.is_valid())

    # Test to check default post code is not require
    def test_default_postcode_is_not_required(self):
        form = UserProfileForm({'default_postcode': ''})
        self.assertTrue(form.is_valid())

    # Test to check default country is not required
    def test_default_country_is_not_required(self):
        form = UserProfileForm({'default_country': ''})
        self.assertTrue(form.is_valid())
