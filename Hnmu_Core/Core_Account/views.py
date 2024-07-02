import requests
from django.conf import settings
from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status

from .models import *
from .forms import *
from Hnmu_Core.root_test import *

TPL_THEM_NGUOI_DUNG = 'pages/Core_Account/NguoiDung/ThemNguoiDung.html'
TPL_HOME = 'pages/Core_Account/Home/Home.html'
TPL_LOGIN = 'pages/Core_Account/Login/Login.html'

def getIdU(request):
    # Call the verify-token endpoint on serverToken
    current_url = request.build_absolute_uri()
    print(current_url)

    verify_url = f'{settings.SERVER_TOKEN_URL}/API/check_token/'
    response = requests.post(verify_url, cookies=request.COOKIES)

    if response.status_code != 200:
        return 0

    # Store the message in the request
    response_data = response.json()
    msg = response_data.get('msg', '0')
    return msg


def menu_items(request):
    IdU = getIdU(request)

    if IdU == 0:
        # Redirect đến URL khác khi IdU == 0
        return {}

    else:
        u = User.objects.get(id=IdU)
        us = Users.objects.get(user=u)
        account_item = us.HoTen
        menu_items = [
            {
                'url': '#1',
                'name': 'act1'
            },
            {
                'url': '#2',
                'name': 'act2'
            }
        ]
        return {'menu_items': menu_items, 'account_item': account_item}
def CallLogin(username, password):

    # Gọi API để lấy token
    APIresponse = requests.post('http://127.0.0.1:8000/API/get_token/', data={
        'username': username,
        'password': password
    })

    token = None
    status_code = APIresponse.status_code
    if APIresponse.status_code == 200:
        data = APIresponse.json()
        token = data.get('access')

    return status_code, token

def Login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, TPL_LOGIN, {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            status_code, token = CallLogin(username, password)
            if status_code == 200:
                response = redirect('Home')
                response.set_cookie('jwt', str(token), httponly=True, secure=True, samesite='Lax')
                return response
            elif status_code == 400:
                return render(request, TPL_LOGIN, {'form': form, 'error': 'Tài khoản hoặc mật khẩu sai'})
            else:
                return render(request, TPL_LOGIN, {'form': form, 'error': 'Có lỗi xảy ra, vui lòng thưr lại'})

        else:
            # Form không hợp lệ, xử lý lỗi nếu cần
            return render(request, TPL_LOGIN, {'form': form})
    else:
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@login_required_remote
def Home(request):
    return render(request, TPL_HOME)

def ThemNguoiDung(request):
    error_message = None  # Khởi tạo giá trị mặc định của error_message

    if request.method == 'POST':
        users_form = UsersForm(request.POST)

        if users_form.is_valid():
            email = users_form.cleaned_data['Email']
            hoten = users_form.cleaned_data['HoTen']
            cccd = users_form.cleaned_data['CCCD']

            # Kiểm tra nếu các trường cụ thể có giá trị
            if email and hoten and cccd:
                pass_first = 'hnmu1234'
                try:
                    with transaction.atomic():
                        user = User.objects.create_user(
                            username=email,
                            email=email,
                            password=pass_first
                        )
                        user.save()

                        users = users_form.save(commit=False)
                        users.user = user
                        users.save()

                    return HttpResponse("Người dùng đã được thêm thành công")

                except Exception as e:
                    # Xử lý lỗi, ví dụ: ghi log và đặt thông báo lỗi
                    error_message = f"Đã xảy ra lỗi: {str(e)}"
            else:
                error_message = "Một hoặc nhiều trường bắt buộc bị thiếu giá trị."
        else:
            error_message = "Một hoặc nhiều form không hợp lệ."
    else:
        users_form = UsersForm()

    return render(request, TPL_THEM_NGUOI_DUNG, {
        'users_form': users_form,
        'error_message': error_message
    })
