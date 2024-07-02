# views.py
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from .forms import NhomForm
from .my_decorators import *


class Add_Department (APIView):
    def post(self, request):
        msg = getattr(request, 'msg', 'No message')
        form = NhomForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            # Thay đổi giá trị trong instance
            instance.CreatedBy = '8'
            instance.UpdatedBy = '8'

            # Lưu instance vào cơ sở dữ liệu
            instance.save()
            return redirect('some_view_name')


    def get(self, request):
        form = NhomForm()
        return render(request, 'pages/Core_Departments/Departments/Add_Department.html', {'form': form})
