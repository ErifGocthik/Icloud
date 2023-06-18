from django import forms as dj_forms
from django.contrib.auth import forms

from auth.models import CustomUser


class CustomUserRegister(forms.UserCreationForm):
    username = dj_forms.CharField(max_length=32,
                                  min_length=6,
                                  label='Логин')
    email = dj_forms.EmailField(max_length=128,
                                min_length=8,
                                label='Эл. Почта')
    first_name = dj_forms.CharField(max_length=32,
                                    min_length=3,
                                    label='Имя')
    last_name = dj_forms.CharField(max_length=32,
                                   min_length=3,
                                   label='Фамилия')
    password1 = dj_forms.CharField(widget=dj_forms.PasswordInput,
                                   label='Пароль')
    password2 = dj_forms.CharField(widget=dj_forms.PasswordInput,
                                   label='Повторите пароль')

    class Meta:
        model = CustomUser
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, item in self.fields.items():
            item.widget.attrs['class'] = 'form-control'
            item.help_text = ''