from django.core.cache import cache
from django.utils import timezone

from accounts.models import User


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def last_visit(self, request):
        key = "recently-seen-{}".format(request.session.session_key)
        recently_seen = cache.get('key')

        if not key and request.user.is_authenticated:
            User.objects.get(id=request.user.id).update()

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        return response