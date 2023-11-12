from django.test import TestCase, Client
from my_streaks.models import Streak
from django.contrib.auth.models import User
from datetime import date


class TestModels(TestCase):

    def setUp(self) -> None:
        self.client = Client()

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.streak = Streak.objects.create(
            name='Test Streak',
            description='Test Description',
            user=self.user
        )


    def tearDown(self) -> None:
        """Delete the user."""
        self.user.delete()
        self.streak.delete()

    def test_streak_days(self):
        """Test that the streak_days property returns the correct number of days."""
        self.assertEquals(self.streak.streak_days, 0)


    def test_is_streak_active(self):
        """Test that the is_streak_active property returns the correct value."""
        self.assertEquals(self.streak.is_streak_active, True)
        self.streak.cancel_streak()
        self.assertEquals(self.streak.is_streak_active, False)
        self.streak.restart_streak()
        self.assertEquals(self.streak.is_streak_active, True)


    def test_is_streak_updated(self):
        """Test that the is_streak_updated property returns the correct value."""
        self.assertEquals(self.streak.is_updated, True)


    def test_start_date(self):
        """Test if the start_date is today."""
        self.assertEquals(self.streak.start_date, date.today())


    def test_latest_streak_date(self):
        """Test if the latest_streak_date is today."""
        self.assertEquals(self.streak.latest_streak_date, date.today())
