from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_success(self):
        email = 'test@yahoo.com'
        password = 'pass1234'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalize(self):
        email = 'test@YAHOO.COM'
        user = get_user_model().objects.create_user(email, 'pass1234')
        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')


    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser('test@yahoo.com', 'test123')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)