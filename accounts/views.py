from django.shortcuts import render

from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:signup_success')
    def form_valid(self, form):
        user = form.save()
        self.object = user
        
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"
    


def logout_view(request):
    logout(request)
    return redirect(reverse('promptapp:index'))


class PrivacypolicyView(TemplateView):
    template_name = "privacypolicy.html"