from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from auth.forms import CustomUserRegister
from auth.models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserRegister
    template_name = 'auth/register.html'
    success_url = reverse_lazy('cloud:cloud_list')

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        if self.form_class(request.POST).is_valid():
            # return redirect(reverse('auth:register'))
            message = render(request, 'auth/verify_register.html')
            send_mail('Регистрация на сайте лучшего интернет-магазина бабы зины',
                      message='Для подтверждения перейдите по сслке',
                      from_email=settings.EMAIL_HOST_USER,
                      # html_message='',
                      recipient_list=[request.POST.get('email')])
        return result
