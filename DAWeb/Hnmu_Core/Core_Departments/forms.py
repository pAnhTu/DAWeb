# forms.py
from django import forms
from .models import Nhom

class NhomForm(forms.ModelForm):
    class Meta:
        model = Nhom
        exclude = ['CreatedBy', 'UpdatedBy']  # Loại bỏ các trường không cần thiết
        labels = {
            'Parent': 'Nhóm Cha',
            'TenNhom': 'Tên Nhóm',
            'MaNhom': 'Mã Nhóm',
            'LoaiNhom': 'Loại Nhóm',
            'Expired': 'Ngày hết hạn',
            'IsActive': 'Trạng Thái Hoạt Động',
            'NienKhoa': 'Niên Khóa',
            'CreatedAt': 'Ngày Tạo',
            'UpdatedAt': 'Ngày Cập Nhật',
        }
        widgets = {
            'CreatedAt': forms.DateTimeInput(attrs={'readonly': 'readonly'}),
            'UpdatedAt': forms.DateTimeInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(NhomForm, self).__init__(*args, **kwargs)
        self.fields['Parent'].required = False
        self.fields['LoaiNhom'].required = False
        self.fields['NienKhoa'].required = False
        self.fields['Expired'].required = False
