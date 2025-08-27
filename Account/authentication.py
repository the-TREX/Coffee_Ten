from django.contrib.auth.backends import BaseBackend
from .models import User

class PhoneOrEmailBackend(BaseBackend):
    """
    اجازه می‌دهد کاربر با شماره تلفن یا ایمیل وارد شود.
    """
    def authenticate(self, request, username=None, password=None):
        user = None
        # ابتدا با شماره تلفن امتحان کن
        try:
            user = User.objects.get(phone=username)
        except User.DoesNotExist:
            # اگر شماره نبود، ایمیل رو امتحان کن
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                return None

        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
