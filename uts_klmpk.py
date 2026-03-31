class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, nama, harga, stok, harga_modal, kategori):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok
        self.__harga_modal = harga_modal
        self.__kategori = kategori

    # Getter
    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def get_kategori(self):
        return self.__kategori

    # Setter (kontrol akses)
    def set_harga(self, harga):
        if harga > 0:
            self.__harga = harga

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.__stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah <= self.__stok:
            self.__stok -= jumlah
        else:
            raise ValueError("Stok tidak cukup")

    @abstractmethod
    def info(self):
        pass

class Makanan(Item):
    def info(self):
        return f"Makanan: {self.get_nama()}"

class Minuman(Item):
    def info(self):
        return f"Minuman: {self.get_nama()}"

class RumahTangga(Item):
    def info(self):
        return f"Rumah Tangga: {self.get_nama()}"
    
class Inventory(LoggerMixin):
    def __init__(self):
        self.__barang = []

    def tambah_barang(self, item):
        self.__barang.append(item)
        self.log(f"Barang {item.get_nama()} ditambahkan")

    def hapus_barang(self, nama):
        self.__barang = [b for b in self.__barang if b.get_nama() != nama]
        self.log(f"Barang {nama} dihapus")

    def cari_barang(self, nama):
        for b in self.__barang:
            if b.get_nama() == nama:
                return b
        return None

    def laporan_stok(self):
        return [(b.get_nama(), b.get_stok()) for b in self.__barang]
    
class Transaksi(LoggerMixin):
    def __init__(self):
        self.__riwayat = []

    def beli(self, item, jumlah):
        item.kurangi_stok(jumlah)
        total = item.get_harga() * jumlah
        self.__riwayat.append((item.get_nama(), jumlah, total))
        self.log(f"Transaksi {item.get_nama()} sebanyak {jumlah}")
        return total

    def laporan_transaksi(self):
        return self.__riwayat
    
class Laporan:
    def __init__(self, inventory, transaksi):
        self.inventory = inventory
        self.transaksi = transaksi

    def tampilkan_laporan(self):
        print("=== STOK ===")
        for nama, stok in self.inventory.laporan_stok():
            print(nama, stok)

        print("\n=== TRANSAKSI ===")
        for data in self.transaksi.laporan_transaksi():
            print(data)