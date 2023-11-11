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

        self.streak = Streak.objects.create(
            name='Test Streak',
            description='Test Description',
            user=self.user
        )

        self.client.login(username='testuser', password='testpassword')

    def tearDown(self):
        """Delete the user."""
        self.user.delete()
        self.streak.delete()

    def test_streak_list_GET(self):
        """Test that the streak list view returns the correct template."""
        response = self.client.get(reverse('streak_list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_streaks/streak_list.html')

    def test_create_streak_GET(self):
        """Test that the create streak view returns the correct template when logged in."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_streak'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_streaks/create_streak.html')

    def test_create_streak_POST(self):
        """Test that the create streak view creates a new streak."""
        streak_name = 'Test Streak'
        streak_description = 'Test Description'

        response = self.client.post(reverse('create_streak'), {
            'name': streak_name,
            'description': streak_description
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('streak_list'))
        self.assertEquals(Streak.objects.filter(user=self.user).first().name, streak_name)
        self.assertEquals(Streak.objects.filter(user=self.user).first().description, streak_description)
        Streak.objects.filter(user=self.user).first().delete()

    def test_check_in_streak_POST(self):
        """Test that the check in streak view updates the streak."""
        response = self.client.post(reverse('check_in_streak'), {
            'streak_id': self.streak.id
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('streak_list'))
        self.assertEquals(Streak.objects.filter(user=self.user).first().latest_streak_date, self.streak.latest_streak_date)

    def test_cancel_streak_POST(self):
        """Test that the cancel streak view cancels the streak."""
        response = self.client.post(reverse('cancel_streak'), {
            'streak_id': self.streak.id
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('streak_list'))
        self.assertEquals(Streak.objects.filter(user=self.user).first().is_canceled, True)

    def test_delete_streak_POST(self):
        """Test that the delete streak view deletes the streak."""
        response = self.client.post(reverse('delete_streak'), {
            'streak_id': self.streak.id
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('streak_list'))
        self.assertEquals(Streak.objects.filter(user=self.user).first(), None)

    def test_restart_streak_POST(self):
        """Test that the restart streak view restarts the streak."""
        self.test_cancel_streak_POST()
        response = self.client.post(reverse('restart_streak'), {
            'streak_id': self.streak.id
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('streak_list'))
        self.assertEquals(Streak.objects.filter(user=self.user).first().is_canceled, False)
