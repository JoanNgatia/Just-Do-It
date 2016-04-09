from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator


class IndexView(TemplateView):
    template_name = 'bucketlists.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        """Add csrf protection to all decorated class views."""
        return super(IndexView, self).dispatch(*args, **kwargs)
