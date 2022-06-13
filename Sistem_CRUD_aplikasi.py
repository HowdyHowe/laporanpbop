from Dictionary import stok_produk

class Sistem_CRUD_aplikasi:
    def __init__(self, data=None, jumlah=None):
        self.data = data
        self.jumlah = jumlah

    def _create(self):
        stok_produk[self.data] = self.jumlah

    def read(self):
        if len(stok_produk) != 0:
            for i in stok_produk:
                n = stok_produk.get(i)
                print(f'•{i} : {n}')
        else:
            print("Tidak ada data di dalam database!")

    def _update(self):
        try:
            i = stok_produk[self.data]
            if i != None:
                stok_produk.update({self.data: self.jumlah})
        except KeyError:
            print("Data yang anda masukkan tidak ada!")

    def _delete(self):
        try:
            i = stok_produk[self.data]
            if i != None:
                del stok_produk[self.data]
                print("Data telah dihapus")
        except KeyError:
            print("Data yang anda masukkan tidak ada!")
