from django.db import models
from django.utils import timezone


# class DM_TrinhDoDaoTao:
#     Id = models.AutoField(primary_key=True)

#
# class DM_HinhThucDaoTao:
#     Id = models.AutoField(primary_key=True)
#
# class DM_LoaiHinhDaoTao:
#     Id = models.AutoField(primary_key=True)
#     TrinhDoDaoTao = models.ForeignKey(DM_TrinhDoDaoTao)
#     HinhThucDaoTao = models.ForeignKey(DM_HinhThucDaoTao)

#
# class ChuongTrinh:
#     Id = models.AutoField(primary_key=True)
#     IdNganhDaoTao = models.IntegerField()
#     LoaiHinhDaoTao = models.ForeignKey(DM_LoaiHinhDaoTao)


class LoaiNhom(models.Model):
    # Định nghĩa các trường cho bảng LoaiNhom
    Id = models.AutoField(primary_key=True)
    IsPhongBan = models.IntegerField(default=0)
    Parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='LN_Parent')  # Sử dụng 'self' thay vì 'LoaiNhom'
    TenLoaiNhom = models.CharField(max_length=255)  # Thêm max_length cho CharField
    CreatedAt = models.DateTimeField(default=timezone.now)  # Sử dụng auto_now_add để tự động đặt giá trị khi tạo bản ghi
    UpdatedAt = models.DateTimeField(default=timezone.now)  # Sử dụng auto_now để tự động cập nhật giá trị khi cập nhật bản ghi
    CreatedBy = models.ForeignKey('Core_Account.Users', on_delete=models.CASCADE, related_name='LN_CreatedBy')  # Sử dụng 'related_name' để tránh xung đột tên
    UpdatedBy = models.ForeignKey('Core_Account.Users', on_delete=models.CASCADE, related_name='LN_UpdatedBy')  # Sử dụng 'related_name' để tránh xung đột tên
    IsActive = models.IntegerField(default=1)

    def __str__(self):
        return self.TenLoaiNhom

    class Meta:
        db_table = 'LoaiNhom'


class Nhom(models.Model):
    # Thong Tin Co Ban
    Id = models.AutoField(primary_key=True)
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='N_Parent')
    TenNhom = models.CharField(max_length=255)  # Thêm max_length cho CharField
    MaNhom = models.CharField(max_length=100)   # Thêm max_length cho CharField
    LoaiNhom = models.ForeignKey('LoaiNhom', on_delete=models.CASCADE)  # Thêm dấu nháy đơn vào 'LoaiNhom'
    Expired = models.DateTimeField(null=True, blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)  # Sử dụng auto_now_add để tự động đặt giá trị khi tạo bản ghi
    UpdatedAt = models.DateTimeField(auto_now=True)      # Sử dụng auto_now để tự động cập nhật giá trị khi cập nhật bản ghi
    CreatedBy = models.ForeignKey('Core_Account.Users', on_delete=models.CASCADE, related_name='N_CreatedBy')  # Sử dụng 'related_name' để tránh xung đột tên
    UpdatedBy = models.ForeignKey('Core_Account.Users', on_delete=models.CASCADE, related_name='N_UpdatedBy')  # Sử dụng 'related_name' để tránh xung đột tên
    IsActive = models.IntegerField(default=1)

    # Thong Tin Nhom La Lop Hanh Chinh
    NienKhoa = models.IntegerField(null=True, blank=True)
    # IdChuongTrinh = models.IntegerField(null=True)
    def __str__(self):
        return self.TenNhom

    class Meta:
        db_table = 'Nhom'
