from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from my_streaks.models import Streak



class TestViews(TestCase):

    def setUp(self):
        """Create a user and log them in."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def tearDown(self):
        """Delete the user."""
        self.user.delete()

    def test_streak_list_GET(self):
        """Test that the streak list view returns the correct template."""
        response = self.client.get(reverse('streak_list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_streaks/streak_list.html')

    def test_create_streak_GET(self):
        """Test that the create streak view returns the correct template."""
        response = self.client.get(reverse('create_streak'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_streaks/create_streak.html')

    def test_create_streak_logged_in_GET(self):
        """Test that the create streak view returns the correct template when logged in."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_streak'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_streaks/create_streak.html')

    def test_create_streak_POST(self):
        """Test that the create streak view creates a new streak."""
        streak_name = 'Test Streak'
        streak_description = 'Test Description'

        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('create_streak'), {
            'name': streak_name,
            'description': streak_description
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('streak_list'))
        self.assertEquals(Streak.objects.filter(user=self.user).first().name, streak_name)
        self.assertEquals(Streak.objects.filter(user=self.user).first().description, streak_description)

