from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()


class UserProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='testpassword'
        )

    def setUp(self):
        self.profile = UserProfile(user=self.user)

    def test_generate_default_username(self):
        generated_username = self.profile.generate_default_username()
        expected_username = f"User000{self.user.id}"
        self.assertEqual(generated_username, expected_username)

    def test_save_with_new_profile(self):
        self.profile.save()
        expected_username = f"User000{self.user.id}"
        self.assertEqual(self.profile.username, expected_username)

    def test_save_with_existing_profile(self):
        existing_profile = UserProfile.objects.create(
            user=self.user,
            username='ExistingUsername',
            bio='ExistingBio'
        )
        existing_profile.save()
        self.assertEqual(existing_profile.username, 'ExistingUsername')

    def test_str_representation(self):
        profile = UserProfile.objects.create(user=self.user)
        self.assertEqual(str(profile), self.user.email)