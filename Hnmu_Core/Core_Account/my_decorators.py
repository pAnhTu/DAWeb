# serverCore/decorators.py
import requests
from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import REDIRECT_FIELD_NAME

def login_required_remote(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/Account/Login/'
):
    """
    Decorator for views that checks that the user is logged in on a remote server,
    redirecting to the log-in page if necessary.
    """
    actual_decorator = user_passes_test_remote(
        lambda u: u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def user_passes_test_remote(test_func, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Check if the user passes a given test on a remote server.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            # Call the remote server endpoint to check authentication
            verify_url = f'{settings.SERVER_TOKEN_URL}/API/check_token/'
            response = requests.post(verify_url, cookies=request.COOKIES)

            if response.status_code != 200:
                return redirect_to_login(
                    request.get_full_path(),
                    login_url=login_url or settings.LOGIN_URL,
                    redirect_field_name=redirect_field_name,
                )

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator