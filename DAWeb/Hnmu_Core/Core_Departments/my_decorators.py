# serverCore/decorators.py
import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status


def token_required(view_func):
    def _wrapped_view(view_instance, request, *args, **kwargs):

        # Call the verify-token endpoint on serverToken
        verify_url = f'{settings.SERVER_TOKEN_URL}/API/check_token/'
        response = requests.post(verify_url, cookies=request.COOKIES)

        if response.status_code != 200:
            response_data = response.json()
            error_message = response_data.get('msg', 'Token verification failed')
            return Response({'error': error_message}, status=response.status_code)

        # Store the message in the request
        response_data = response.json()
        request.msg = response_data.get('msg', 'Token is valid')

        return view_func(view_instance, request, *args, **kwargs)

    return _wrapped_view