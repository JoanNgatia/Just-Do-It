"""Define django view for auhtentication and dashboard info."""
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext
# from bucketlist.forms.form_authentication import LoginForm, RegistrationForm

from bucketlist.forms import RegistrationForm


class IndexView(TemplateView):
    """Base view where they will all inherit data from."""

    template_name = 'bucketlists/dashboard.html'

    def get_context_data(self, **kwargs):
        """Return dictionary representing passed in context."""
        context = super(IndexView, self).get_context_data(**kwargs)
        context['registrationform'] = RegistrationForm()
        return context


class RegistrationView(IndexView):
    """Define Registration view on template."""

    form_class = RegistrationForm

    def post(self, request, **kwargs):
        """Method to create a new user."""
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=request.POST['username'],
                password=request.POST['password'])
            login(request, new_user)
            messages.success(
                request, 'Registration successful!!')
            return redirect(
                '/bucketlist',
                context_instance=RequestContext(request)
            )
        else:
            messages.error(
                request, 'Error at registration!')
            return redirect(
                '/register',
                context_instance=RequestContext(request)
            )
