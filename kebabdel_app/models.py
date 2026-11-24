from django.db import models

class Pesanan(models.Model):
    """
    Represents a pesanan in the system.
    """
    idPesanan =  models.IntegerField()
    waktuPesan =  models.DateTimeField()
    jenisLayanan =  models.CharField(max_length=255)
    statusPesanan =  models.CharField(max_length=255)
    totalHarga =  models.IntegerField()
    alamatdelivery = models.ForeignKey(
        'AlamatDelivery', related_name='pesanan', on_delete=models.SET_NULL, blank=True, null=True)
    koki = models.ForeignKey(
        'Koki', related_name='pesanan', on_delete=models.SET_NULL, blank=True, null=True)
    menu = models.ManyToManyField(
        'Menu', related_name='pesanan')
    outlet = models.ForeignKey(
        'Outlet', related_name='pesanan', on_delete=models.PROTECT)
    pelanggan = models.ForeignKey(
        'Pelanggan', related_name='pesanan', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Pesanan"
        verbose_name_plural = "Pesanans"
    def __str__(self):
        """
        Returns a string representation of the pesanan
        """
        return str(self.idPesanan)
class Pengguna(models.Model):
    """
    Represents a pengguna in the system.
    """
    idPengguna =  models.IntegerField()
    namaLengkap =  models.CharField(max_length=255)
    nomorTelepon =  models.CharField(max_length=255)

    class Meta:
        verbose_name = "Pengguna"
        verbose_name_plural = "Penggunas"
    def __str__(self):
        """
        Returns a string representation of the pengguna
        """
        return str(self.idPengguna)
class Pembayaran(models.Model):
    """
    Represents a pembayaran in the system.
    """
    idPembayaran =  models.IntegerField()
    waktuBayar =  models.DateTimeField()
    metodeBayar =  models.CharField(max_length=255)
    statusBayar =  models.CharField(max_length=255)
    pesanan = models.OneToOneField(
        'Pesanan', related_name='pembayaran', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Pembayaran"
        verbose_name_plural = "Pembayarans"
    def __str__(self):
        """
        Returns a string representation of the pembayaran
        """
        return str(self.idPembayaran)
class Pelanggan(Pengguna):
    """
    Represents a pelanggan in the system.
    """
    email =  models.CharField(max_length=255)

    class Meta:
        verbose_name = "Pelanggan"
        verbose_name_plural = "Pelanggans"
    def __str__(self):
        """
        Returns a string representation of the pelanggan
        """
        return str(self.email)
class Outlet(models.Model):
    """
    Represents a outlet in the system.
    """
    idOutlet =  models.IntegerField()
    namaOutlet =  models.CharField(max_length=255)
    lokasiOutlet =  models.CharField(max_length=255)
    menu = models.ManyToManyField(
        'Menu', related_name='outlet')

    class Meta:
        verbose_name = "Outlet"
        verbose_name_plural = "Outlets"
    def __str__(self):
        """
        Returns a string representation of the outlet
        """
        return str(self.idOutlet)
class MenuOutlet(models.Model):
    """
    Represents a menuOutlet in the system.
    """
    statusTersedia =  models.BooleanField()

    class Meta:
        verbose_name = "MenuOutlet"
        verbose_name_plural = "MenuOutlets"
    def __str__(self):
        """
        Returns a string representation of the menuOutlet
        """
        return str(self.statusTersedia)
class Menu(models.Model):
    """
    Represents a menu in the system.
    """
    idMenu =  models.IntegerField()
    namaMenu =  models.CharField(max_length=255)
    hargaDasar =  models.IntegerField()
    deskripsi =  models.CharField(max_length=255)

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
    def __str__(self):
        """
        Returns a string representation of the menu
        """
        return str(self.idMenu)
class Koki(Pengguna):
    """
    Represents a koki in the system.
    """
    nipKoki =  models.CharField(max_length=255)
    outlet = models.ForeignKey(
        'Outlet', related_name='koki', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Koki"
        verbose_name_plural = "Kokis"
    def __str__(self):
        """
        Returns a string representation of the koki
        """
        return str(self.nipKoki)
class DetailPesanan(models.Model):
    """
    Represents a detailPesanan in the system.
    """
    kuantitas =  models.IntegerField()
    subTotal =  models.IntegerField()

    class Meta:
        verbose_name = "DetailPesanan"
        verbose_name_plural = "DetailPesanans"
    def __str__(self):
        """
        Returns a string representation of the detailPesanan
        """
        return str(self.kuantitas)
class AlamatDelivery(models.Model):
    """
    Represents a alamatDelivery in the system.
    """
    idAlamat =  models.IntegerField()
    detailAlamat =  models.CharField(max_length=255)
    pelanggan = models.ForeignKey(
        'Pelanggan', related_name='alamatdelivery', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "AlamatDelivery"
        verbose_name_plural = "AlamatDeliverys"
    def __str__(self):
        """
        Returns a string representation of the alamatDelivery
        """
        return str(self.idAlamat)
