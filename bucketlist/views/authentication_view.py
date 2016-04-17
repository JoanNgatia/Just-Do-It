"""Define django view for authentication and dashboard info."""
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.template import RequestContext

from bucketlist.forms.forms_authentication import RegistrationForm, LoginForm


class IndexView(TemplateView):
    """Base view where they will all inherit data from."""

    template_name = 'bucketlists/dashboard.html'

    def get_context_data(self, **kwargs):
        """Return dictionary representing passed in context."""
        context = super(IndexView, self).get_context_data(**kwargs)
        context['registrationform'] = RegistrationForm()
        context['loginform'] = LoginForm()
        return context


class RegistrationView(IndexView):
    """Define Registration view on template."""

    form_class = RegistrationForm

    def post(self, request, **kwargs):
        """Method to create a new user."""
        # Check that method is post to access data passed
        form = self.form_class(request.POST)
        if form.is_valid():
            # save data passed into the database
            new_user = form.save()
            new_user = authenticate(
                username=request.POST['username'],
                password=request.POST['password'])
            login(request, new_user)
            messages.success(
                request, 'Registration successful!!')
            return redirect(
                '/bucketlists',
                context_instance=RequestContext(request)
            )
        else:
            messages.error(
                request, 'Error at registration!')
            return redirect(
                '/register',
                context_instance=RequestContext(request)
            )


class LoginView(IndexView):
    """Define login on index template view."""

    form_class = LoginForm

    def post(self, request, **kwargs):
        """Method to login a registered user."""
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                messages.success(
                    request, 'Welcome Back!!')
                return redirect(
                    '/bucketlists',
                    context_instance=RequestContext(request)
                )
            else:
                messages.error(
                    request, 'Incorrect username or password!')
                return redirect(
                    '/login',
                    context_instance=RequestContext(request)
                )
        else:
            context = super(LoginView, self).get_context_data(**kwargs)
            context['loginform'] = form
            return render(request, self.template_name, context)
