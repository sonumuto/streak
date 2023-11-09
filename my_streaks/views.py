from datetime import date
from typing import Any
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Streak
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
class StreakListView(ListView):
    model = Streak
    template_name = 'streak_list.html'
    context_object_name = 'streaks'


class CreateStreakView(CreateView):
    model = Streak
    template_name = 'my_streaks/create_streak.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('streak_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CheckInStreakView(View):
    def post(self, request):
        review_id = request.POST["streak_id"]
        Streak.objects.get(id=review_id).update_streak()
        # redirect to streak list
        success_url = reverse_lazy('streak_list')

        return HttpResponseRedirect(success_url)


class CancelStreakView(View):
    def post(self, request):
        review_id = request.POST["streak_id"]

        Streak.objects.get(id=review_id).cancel_streak()
        # redirect to streak list
        success_url = reverse_lazy('streak_list')

        return HttpResponseRedirect(success_url)


class DeleteStreakView(View):
    def post(self, request):
        review_id = request.POST["streak_id"]

        Streak.objects.get(id=review_id).delete()
        # redirect to streak list
        success_url = reverse_lazy('streak_list')

        return HttpResponseRedirect(success_url)


class RestartStreakView(View):
    def post(self, request):
        review_id = request.POST["streak_id"]

        Streak.objects.get(id=review_id).restart_streak()
        # redirect to streak list
        success_url = reverse_lazy('streak_list')

        return HttpResponseRedirect(success_url)