from django.urls import path
from . import views

urlpatterns = [
    path('', views.StreakListView.as_view(), name='streak_list'),
    path('create/', views.CreateStreakView.as_view(), name='create_streak'),
    path('update/', views.CheckInStreakView.as_view(), name='update_streak'),
    path('cancel/', views.CancelStreakView.as_view(), name='cancel_streak'),
    path('restart/', views.RestartStreakView.as_view(), name='restart_streak'),
    path('delete/', views.DeleteStreakView.as_view(), name='delete_streak'),
]
