from django.urls import path

from auth.views import RegisterView

app_name = 'custom_auth'

urlpatterns = [
    path('sign-up/', RegisterView.as_view(), name='register'),
]