from django.urls import path

from form_profile.views import ProfileCreateView

app_name = 'form_profile'


urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create')
]