# ================================
# DATA PRODUK
# tipe data : Dictionary of Dictionary
# Struktur: {ID: {"nama": str, "berat": int (gram), "harga": int (rupiah)}}
# ================================
produk_dict = {
    1: {"nama": "Tomat", "berat": 500, "harga": 8000},
    2: {"nama": "Cabai rawit Merah", "berat": 150, "harga": 30000},
    3: {"nama": "Cabai keriting Merah", "berat": 150, "harga": 25000},
    4: {"nama": "Bawang Merah", "berat": 250, "harga": 17900},
    5: {"nama": "Bawang Putih", "berat": 250, "harga": 16000},
    6: {"nama": "Bawang bombay", "berat": 400, "harga": 36000},
    7: {"nama": "Buncis", "berat": 200, "harga": 7500},
    8: {"nama": "Pakcoy", "berat": 150, "harga": 4900},
    9: {"nama": "Wortel", "berat": 500, "harga": 15400},
    10: {"nama": "Kangkung", "berat": 200, "harga": 5300},
    11: {"nama": "Terong ungu", "berat": 450, "harga": 9000},
    12: {"nama": "Timun", "berat": 500, "harga": 10800},
    13: {"nama": "Kol", "berat": 1000, "harga": 23800},
    14: {"nama": "Sawi putih", "berat": 600, "harga": 1200},
}

# ================================
# KERANJANG BELANJA → pakai dictionary
# Struktur: {nama_produk: {"harga": int, "qty": int, "berat": int}}
# ================================
keranjang = {}

# ================================
# FUNGSI INPUT ANGKA (lebih efisien)
# ================================
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input harus berupa angka!\n")

# ================================
# FUNGSI: Tampilkan semua produk
# ================================
def tampilkan_produk():
    print("\n=== DAFTAR PRODUK ===")
    for id_produk, info in produk_dict.items():
        print(f"{id_produk}. {info['nama']} - {info['berat']} gr - Rp{info['harga']}")
    print()

# ================================
# FUNGSI: Hitung subtotal satu item → harga * qty
# ================================
def hitung_subtotal(item):
    return item['qty'] * item['harga']

# ================================
# FUNGSI: Menampilkan isi keranjang + subtotal per item
# ================================
def tampilkan_keranjang():
    print("\n=== KERANJANG BELANJA ===")
    if not keranjang:
        print("Keranjang kosong.\n")
        return 0
    total = 0
    for i, (nama, item) in enumerate(keranjang.items(), start=1):
        subtotal = hitung_subtotal(item)
        total += subtotal
        print(f"{i}. {nama} x{item['qty']} - {item['berat']} gr - Rp{subtotal}")
    print(f"Total Belanja: Rp{total}\n")
    return total

# ================================
# FUNGSI: Menambah produk ke keranjang
# ================================
def tambah_keranjang():
    while True:
        tampilkan_produk()
        id_pilihan = input_int("Masukkan ID produk yang ingin dibeli: ")
        qty = input_int("Jumlah yang ingin dibeli: ")
        if qty <= 0:
            print("Jumlah harus lebih dari 0.\n")
            continue

        produk = produk_dict.get(id_pilihan)
        if produk:
            nama = produk['nama']
            if nama in keranjang:
                keranjang[nama]['qty'] += qty
            else:
                keranjang[nama] = {
                    "harga": produk['harga'],
                    "qty": qty,
                    "berat": produk['berat']
                }
            print(f"{nama} berhasil ditambahkan ke keranjang.\n")
        else:
            print("Produk tidak ditemukan.\n")

        if input("Tambah produk lain? (y/n): ").lower() != "y":
            break

# ================================
# FUNGSI: Menghapus item dari keranjang
# ================================
def hapus_keranjang():
    total = tampilkan_keranjang()
    if total == 0:
        return

    nama_list = list(keranjang.keys())
    idx = input_int("Masukkan nomor item yang ingin dihapus: ") - 1
    if 0 <= idx < len(nama_list):
        nama = nama_list[idx]
        konfirmasi = input(f"Yakin ingin menghapus {nama}? (y/n): ").lower()
        if konfirmasi == "y":
            del keranjang[nama]
            print("Item berhasil dihapus.\n")
        else:
            print("Penghapusan dibatalkan.\n")
    else:
        print("Nomor item tidak valid.\n")

# ================================
# FUNGSI: Mengubah jumlah item di keranjang
# ================================
def ubah_jumlah_keranjang():
    total = tampilkan_keranjang()
    if total == 0:
        return

    nama_list = list(keranjang.keys())
    idx = input_int("Masukkan nomor item yang ingin diubah jumlahnya: ") - 1
    if 0 <= idx < len(nama_list):
        nama = nama_list[idx]
        while True:
            qty_baru = input_int(f"Masukkan jumlah baru untuk {nama}: ")
            if qty_baru <= 0:
                print("Jumlah harus lebih dari 0.\n")
            else:
                keranjang[nama]['qty'] = qty_baru
                print("Jumlah berhasil diubah.\n")
                break
    else:
        print("Nomor item tidak valid.\n")

# ================================
# FUNGSI: Checkout transaksi
# ================================
def checkout():
    total = tampilkan_keranjang()
    if total == 0:
        return
    if input("Lanjutkan ke checkout? (y/n): ").lower() == "y":
        print("Checkout berhasil! Terima kasih telah berbelanja.\n")
        keranjang.clear()
    else:
        print("Checkout dibatalkan.\n")

# ================================
# FUNGSI: Menu utama aplikasi
# ================================
def main_menu():
    while True:
        print("=== APLIKASI BELANJA SAYUR ===")
        print("1. Lihat Produk")
        print("2. Tambah ke Keranjang")
        print("3. Lihat Keranjang")
        print("4. Hapus dari Keranjang")
        print("5. Ubah Jumlah di Keranjang")
        print("6. Checkout")
        print("7. Keluar")

        pilihan = input("Pilih menu (1-7): ")
        if pilihan == "1":
            tampilkan_produk()
        elif pilihan == "2":
            tambah_keranjang()
        elif pilihan == "3":
            tampilkan_keranjang()
        elif pilihan == "4":
            hapus_keranjang()
        elif pilihan == "5":
            ubah_jumlah_keranjang()
        elif pilihan == "6":
            checkout()
        elif pilihan == "7":
            print("Sampai jumpa, semoga harimu menyenangkan!\n")
            break
        else:
            print("Pilihan tidak valid.\n")

# ================================
# JALANKAN PROGRAM
# ================================
main_menu()
