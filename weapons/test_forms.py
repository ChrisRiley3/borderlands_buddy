from django.test import TestCase
from .forms import WeaponForm


class TestWeaponForm(TestCase):

    def test_category_is_required(self):
        form = WeaponForm({'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')

    def test_name_required(self):
        form = WeaponForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_description_is_required(self):
        form = WeaponForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_manufacture_is_required(self):
        form = WeaponForm({'manufacture': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('manufacture', form.errors.keys())
        self.assertEqual(form.errors['manufacture'][0], 'This field is required.')

    def test_price_is_required(self):
        form = WeaponForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_image_url_is_required(self):
        form = WeaponForm({'image_url': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('image_url', form.errors.keys())
        self.assertEqual(form.errors['image_url'][0], 'This field is required.')

