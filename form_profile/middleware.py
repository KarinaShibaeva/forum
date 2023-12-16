from django.utils.deprecation import MiddlewareMixin

from form_profile.models import Profile


class RequiredProfileMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user

        if user.is_authenticated:
            return None

        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            return None

        return None