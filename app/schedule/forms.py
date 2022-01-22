from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string

from .models import RegisterService


class RegisterForm(forms.Form):
    email = forms.EmailField(label='Электронная почта')
    service_name = forms.CharField(max_length=72, label='Название сервиса')
    service_desc = forms.CharField(widget=forms.Textarea, label ='Описание сервиса')

    def send_email(self, form):
        rand_user = get_random_string()
        rand_password = get_random_string()
        user = User.objects.create_user(rand_user, form.cleaned_data['email'], rand_password)
        service_obj = RegisterService.objects.create(user=user,
                                                     service_name=form.cleaned_data['service_name'],
                                                     service_desc=form.cleaned_data['service_desc'])
        service_obj.save()

        email = EmailMessage(subject='Данные для подключения к сервису API расписания',
                             body='Добрый день, данные для подключения к сервису ниже:\nПользователь: {}, Пароль: {}\n\nHappy coding!'.format(
                rand_user, rand_password),
                             from_email=settings.EMAIL_HOST_USER,
                             to=[form.cleaned_data['email']],
                             bcc=None,
                             connection=None,
                             attachments=None,
                             headers=None,
                             cc=None,
                             reply_to=[settings.EMAIL_HOST_USER])
        email.send()
