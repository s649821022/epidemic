from django.dispatch import Signal

# New user has registered. Args: user, request.
user_registered = Signal()
user_password_changed = Signal()
user_activated = Signal()
