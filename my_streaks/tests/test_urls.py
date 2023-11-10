from django.test import SimpleTestCase
from django.urls import reverse, resolve
import my_streaks.views as views


class TestUrls(SimpleTestCase):
    """Test that the urls resolve to the correct views."""

    def test_streak_list_url_resolves(self):
        """Streak List URL resolves to the Streak List View."""
        url = reverse('streak_list')
        self.assertEqual(resolve(url).func.view_class, views.StreakListView)

    def test_create_streak_url_resolves(self):
        """Create Streak URL resolves to the Create Streak View."""
        url = reverse('create_streak')
        self.assertEqual(resolve(url).func.view_class, views.CreateStreakView)

    def test_check_in_streak_url_resolves(self):
        """Check In Streak URL resolves to the Check In Streak View."""
        url = reverse('update_streak')
        self.assertEqual(resolve(url).func.view_class, views.CheckInStreakView)

    def test_cancel_streak_url_resolves(self):
        """Cancel Streak URL resolves to the Cancel Streak View."""
        url = reverse('cancel_streak')
        self.assertEqual(resolve(url).func.view_class, views.CancelStreakView)

    def test_restart_streak_url_resolves(self):
        """Restart Streak URL resolves to the Restart Streak View."""
        url = reverse('restart_streak')
        self.assertEqual(resolve(url).func.view_class, views.RestartStreakView)

    def test_delete_streak_url_resolves(self):
        """Delete Streak URL resolves to the Delete Streak View."""
        url = reverse('delete_streak')
        self.assertEqual(resolve(url).func.view_class, views.DeleteStreakView)
