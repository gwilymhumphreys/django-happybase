from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.views import redirect_to_login
from users.models import Customer


INACTIVE_URL = reverse('users:inactive_account')


def active_user_required(function=None, inactive_url=INACTIVE_URL):
    """
    Redirect to a message if this user has not been activated
    """
    def _decorator(view):
        def _decorated(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated():
                return redirect_to_login(request.build_absolute_uri())
            try:
                if not user.customer.active:
                    return HttpResponseRedirect(inactive_url)
            except Customer.DoesNotExist:
                if not user.is_staff:
                    raise NoCustomerException()
                else:
                    # Create a customer object for the staff member
                    cust = Customer(user=user, active=True)
                    cust.save()
            return view(request, *args, **kwargs)
        return _decorated
    if function is None:
        return _decorator
    else:
        return _decorator(function)


class NoCustomerException(Exception):
    pass
