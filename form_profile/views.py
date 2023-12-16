from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from form_profile.forms import ProfileCreationForm
from form_profile.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'form_profile/create_profile.html'
    success_url = reverse_lazy('profile:create')


