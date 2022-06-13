from Sistem_CRUD_aplikasi import Sistem_CRUD_aplikasi

class Aplikasi_stok_toko_buah(Sistem_CRUD_aplikasi):
    def __init__(self, id=None, password=None, data=None, jumlah=None):
        super().__init__(data, jumlah)
        self.id = id
        self.password = password

    def login(self):
        id_admin = "admin"
        pw_admin = "112233"
        id_pt = "pemilik"
        pw_pt = "123456"

        if self.id == id_admin:
            if self.password == pw_admin:
                return "admin"
            else:
                return "ID atau Sandi anda salah!"
        elif self.id == id_pt:
            if self.password == pw_pt:
                return "pemilik"
            else:
                return "ID atau Sandi anda salah!"
        else:
            return "ID atau Sandi anda salah!"
