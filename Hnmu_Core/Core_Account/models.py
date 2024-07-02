from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User as DjangoUser



class Users(models.Model):
    # Định nghĩa các trường cho bảng Users

    #IdHeThong
    Id = models.AutoField(primary_key=True)
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE, related_name='user')
    IdCard = models.CharField(max_length=100, null=True)

    #ThongTinNguoiDung
    HoTen = models.CharField(max_length=100, null=True)
    GioiTinh = models.IntegerField(null=True)
    NgaySinh = models.DateField(null=True)
    DanToc = models.IntegerField(null=True)
    SDT = models.CharField(null=True)
    ThanhPhanXuatThan = models.CharField(max_length=225, null=True)
    IdQuocTich = models.IntegerField(null=True)
    TonGiao = models.CharField(max_length=100, null=True)
    SDT = models.CharField(max_length=20, null=True)
    Email = models.EmailField(null=True)

    #CCCD
    CCCD = models.CharField(max_length=20, null=True)
    NgayCapCCCD = models.DateField(max_length=20, null=True)
    NoiCapCCCD = models.CharField(max_length=20, null=True)


    #Doan/Dang
    NgayVaoDoan = models.DateField(null=True)
    NgayVaoDang = models.DateField(null=True)

    #ThongTinThem
    SoTk = models.CharField(null=True)
    TenNganHang = models.CharField(null=True)
    MaBaoHiem = models.CharField(null=True)
    SoTheThuVien = models.CharField(null=True)

    def __str__(self):
        return self.HoTen

    class Meta:
        db_table = 'Users'


class LyLichBoSung(models.Model):
    Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(Users, on_delete=models.CASCADE)

    #KetQuaHocTap
    XepLoaiHocTap = models.IntegerField(null=True)
    XepLoaiHanhKiem = models.IntegerField(null=True)
    XepLoaiTotNghiep = models.IntegerField(null=True)
    NamTotNghiep = models.IntegerField(null=True)
    DiemThuong = models.FloatField(null=True)
    LyDoThuongDiem = models.CharField(null=True)

    #ThongTinGiaDinh
    #Cha
    HoTenCha = models.CharField(max_length=225, null=True)
    QuocTichCha = models.IntegerField(null=True)
    DanTocCha = models.IntegerField(null=True)
    TonGiaoCha = models.IntegerField(null=True)
    NamSinhCha = models.IntegerField(null=True)
    HoKhauTTCha = models.CharField(max_length=500, null=True)
    NgheNghiepCha = models.CharField(max_length=500, null=True)
    #Me
    HoTenMe = models.CharField(max_length=225, null=True)
    QuocTichMe = models.IntegerField(null=True)
    DanTocMe = models.IntegerField(null=True)
    TonGiaoMe = models.IntegerField(null=True)
    NamSinhMe = models.IntegerField(null=True)
    HoKhauTTMe = models.CharField(max_length=500, null=True)
    NgheNghiepMe = models.CharField(max_length=500, null=True)
    #Vo/Chong
    HoTenVC = models.CharField(max_length=225, null=True)
    QuocTichVC = models.IntegerField(null=True)
    DanTocVC = models.IntegerField(null=True)
    TonGiaoVC = models.IntegerField(null=True)
    NamSinhVC = models.IntegerField(null=True)
    HoKhauTTVC = models.CharField(max_length=500, null=True)
    NgheNghiepVC = models.CharField(max_length=500, null=True)
    #AnhChiEm
    ThongTinACE = models.CharField(max_length=1000, null=True)
    class Meta:
        db_table = 'LyLichBoSung'

class SinhVien(models.Model):
    Id = models.AutoField(primary_key=True)
    Users = models.ForeignKey(Users, on_delete=models.CASCADE)
    MaSinhVien = models.CharField(max_length=50, null=True)
    Status = models.IntegerField(default=1)
    CreateAt = models.DateTimeField(default=timezone.now)
    UpdateAt = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'SinhVien'


class TuyenSinh(models.Model):
    Id = models.AutoField(primary_key=True)
    SinhVien = models.ForeignKey(SinhVien, on_delete=models.CASCADE, related_name='TuyenSinh')
    IdChuongTrinh = models.IntegerField()
    IdLoaiHinhDaoTao = models.IntegerField()
    IdHinhThucDaoTao = models.IntegerField()
    IdTrangThaiHoc = models.IntegerField()
    IdLoaiTotNghiep = models.IntegerField(null=True)
    NgayChuyenTrangThaiHoc = models.DateField(null=True)
    ChuyenNganh = models.IntegerField()
    NgayNhapHoc = models.DateField(null=True)
    KhoaDaoTao = models.IntegerField()
    MaToHopTrungTuyen = models.CharField(null=True)
    DiemTrungTuyen = models.FloatField(null=True)
    MaMon1 = models.CharField(null=True)
    DiemMon1 = models.FloatField(null=True)
    MaMon2 = models.CharField(null=True)
    DiemMon2 = models.FloatField(null=True)
    MaMon3 = models.CharField(null=True)
    DiemMon3 = models.FloatField(null=True)
    DoiTuongUuTien = models.IntegerField(null=True)
    KhuVucUuTien = models.CharField(null=True)
    NamTotNghiepTHPT = models.IntegerField(null=True)
    HocLuc = models.CharField(max_length=20, null=True)
    HanhKiem = models.CharField(max_length=20, null=True)
    MaTinhLop12 = models.CharField(null=True)
    MaQuanLop12 = models.CharField(null=True)
    MaTruongLop12 = models.CharField(null=True)
    DiemTBLop12 = models.FloatField(null=True)
    Status = models.IntegerField(default=1)
    CreateAt = models.DateTimeField(default=timezone.now)
    UpdateAt = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'TuyenSinh'


class DiaChi(models.Model):
    # Định nghĩa các trường cho bảng Users
    Id = models.AutoField(primary_key=True)
    DateStart = models.DateTimeField(null=True)
    DateEnd = models.DateTimeField(null=True)
    IdTinh = models.IntegerField(null=True)
    IdHuyen = models.CharField(max_length=100, null=True)
    IdXa = models.IntegerField(null=True)
    ThonXom = models.CharField(max_length=100, null=True)
    Type = models.IntegerField(null=True)
    Status = models.IntegerField(default=1)

    # Mối quan hệ một một với bảng Users
    User = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

    # Các trường khác nếu cần

    class Meta:
        db_table = 'DiaChi'



