from django.contrib.auth.backends import BaseBackend
from .models import User


class EmailauthBackend(BaseBackend): #in class user ro ba email Login Mikone
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username) # talash Baraye Peida kardan User Az db
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
