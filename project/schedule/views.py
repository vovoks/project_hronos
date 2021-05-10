from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import RegisterForm


class RegisterServiceView(SuccessMessageMixin, FormView):
    template_name = "schedule/register_service.html"
    form_class = RegisterForm
    success_url = '/register-service'
    success_message = "Сервис зарегистрирован, проверьте электронную почту, указанную при регистрации."

    def form_valid(self, form):
        form.send_email(form)
        return super().form_valid(form)
