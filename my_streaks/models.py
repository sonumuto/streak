from datetime import date, timedelta
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Streak(models.Model):
    """Model to represent a streak."""
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    latest_streak_date = models.DateField(auto_now_add=True)
    is_canceled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


    @property
    def streak_days(self) -> int:
        """Return the number of days in the streak."""
        return (self.latest_streak_date - self.start_date).days


    @property
    def is_streak_active(self) -> bool:
        """Return True if the streak is active, False otherwise."""
        print(self.is_canceled)
        if not (self.latest_streak_date == date.today() or self.latest_streak_date == date.today() - timedelta(days=1)):
            self.cancel_streak()
        if self.is_canceled:
            return False
        else:
            return True


    @property
    def is_updated(self) -> bool:
        """Return True if the streak has been updated today, False otherwise."""
        if self.latest_streak_date == date.today():
            return True
        return False


    def check_in_streak(self) -> None:
        """Update the streak."""
        if self.is_streak_active:
            self.latest_streak_date = date.today()
        self.save()


    def cancel_streak(self) -> None:
        """Cancel the streak."""
        self.is_canceled = True
        self.save()


    def restart_streak(self) -> None:
        """Restart the streak."""
        self.is_canceled = False
        self.start_date = date.today()
        self.latest_streak_date = date.today()
        self.save()
