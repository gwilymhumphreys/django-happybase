from django.contrib.auth import login

def force_login(request, user):
    """
    Login user with dirty hacks
    """
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    return user
