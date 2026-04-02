# Import dari uts_klmpk.py
from uts_klmpk import (
    Makanan, Minuman, RumahTangga, 
    Inventory, Transaksi, Laporan
)

# Membuat instance Inventory dan Transaksi
inventory = Inventory()
transaksi = Transaksi()

# Membuat barang-barang
roti = Makanan("Roti", 10000, 10, 5000, "Makanan")
air_mineral = Minuman("Air Mineral", 5000, 20, 2000, "Minuman")
sapu = RumahTangga("Sapu", 15000, 15, 8000, "Rumah Tangga")

# Menambah barang ke inventory
inventory.tambah_barang(roti)
inventory.tambah_barang(air_mineral)
inventory.tambah_barang(sapu)

# Melakukan beberapa transaksi
print("=== MELAKUKAN TRANSAKSI ===")
total1 = transaksi.beli(roti, 2)
print(f"Total: Rp{total1}")

total2 = transaksi.beli(air_mineral, 5)
print(f"Total: Rp{total2}")

total3 = transaksi.beli(sapu, 1)
print(f"Total: Rp{total3}")

# Menampilkan laporan
print("\n")
laporan = Laporan(inventory, transaksi)
laporan.tampilkan_laporan()