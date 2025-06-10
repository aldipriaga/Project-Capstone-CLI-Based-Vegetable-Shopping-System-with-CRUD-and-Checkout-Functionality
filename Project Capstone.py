#Variables
produk_list = [
    {"id": 1, "nama": "Tomat", "berat": 500, "harga": 8000},
    {"id": 2, "nama": "Cabai rawit Merah", "berat": 150, "harga": 30000},
    {"id": 3, "nama": "Cabai keriting Merah", "berat": 150, "harga": 25000},
    {"id": 4, "nama": "Bawang Merah", "berat": 250, "harga": 17900},
    {"id": 5, "nama": "Bawang Putih", "berat": 250, "harga": 16000},
    {"id": 6, "nama": "Bawang bombay", "berat": 400, "harga": 36000},
    {"id": 7, "nama": "Buncis", "berat": 200, "harga": 7500},
    {"id": 8, "nama": "Pakcoy", "berat": 150, "harga": 4900},
    {"id": 9, "nama": "Wortel", "berat": 500, "harga": 15400},
    {"id": 10, "nama": "Kangkung", "berat": 200, "harga": 5300},
    {"id": 11, "nama": "Terong ungu", "berat": 450, "harga": 9000},
    {"id": 12, "nama": "Timun", "berat": 500, "harga": 10800},
    {"id": 13, "nama": "Kol", "berat": 1000, "harga": 23800},
    {"id": 14, "nama": "Sawi putih", "berat": 600, "harga": 1200}
]

keranjang = []

# ======== Lihat Daftar Produk ========
def tampilkan_produk():
    print("\n=== DAFTAR PRODUK ===")
    for produk in produk_list:
        print(f"{produk['id']}. {produk['nama']} - {produk['berat']} gr - Rp{produk['harga']}")
    print()

# ======== Tambah ke Keranjang (CREATE) ========
def tambah_keranjang():
    while True:
        tampilkan_produk()
        try:
            id_pilihan = int(input("Masukkan ID produk yang ingin dibeli: "))
            qty = int(input("Jumlah yang ingin dibeli: "))
            if qty <= 0:
                print("Jumlah harus lebih dari 0.\n")
                continue
            for produk in produk_list:
                if produk['id'] == id_pilihan:
                    keranjang.append({
                        "nama": produk['nama'],
                        "harga": produk['harga'],
                        "qty": qty,
                        "berat": produk['berat']
                    })
                    print(f"{produk['nama']} berhasil ditambahkan ke keranjang.\n")
                    break
            else:
                print("Produk dengan ID tersebut tidak ditemukan.\n")

            lanjut = input("Ingin menambahkan produk lain? (y/n): ").lower()
            if lanjut != "y":
                print("Kembali ke menu utama.\n")
                break

        except ValueError:
            print("Input harus berupa angka!\n")

# ======== Lihat Keranjang (READ) ========
def lihat_keranjang():
    print("\n=== KERANJANG BELANJA ===")
    if not keranjang:
        print("Keranjang kosong.\n")
        return
    total = 0
    for i, item in enumerate(keranjang):
        subtotal = item['harga'] * item['qty']
        total += subtotal
        print(f"{i+1}. {item['nama']} x{item['qty']} - {item['berat']} gr - Rp{subtotal}")
    print(f"Total Belanja: Rp{total}\n")

# ======== Hapus dari Keranjang (DELETE) ========
def hapus_keranjang():
    lihat_keranjang()
    if not keranjang:
        return
    try:
        idx = int(input("Masukkan nomor item yang ingin dihapus: ")) - 1
        if 0 <= idx < len(keranjang):
            konfirmasi = input(f"Yakin ingin menghapus {keranjang[idx]['nama']}? (y/n): ").lower()
            if konfirmasi == "y":
                keranjang.pop(idx)
                print("Item berhasil dihapus.\n")
            else:
                print("Penghapusan dibatalkan.\n")
        else:
            print("Nomor item tidak valid.\n")
    except ValueError:
        print("Input harus angka!\n")

# ======== Ubah Jumlah di Keranjang (UPDATE) ========
def ubah_jumlah_keranjang():
    lihat_keranjang()
    if not keranjang:
        return
    try:
        idx = int(input("Masukkan nomor item yang ingin diubah jumlahnya: ")) - 1
        if 0 <= idx < len(keranjang):
            while True:
                try:
                    qty_baru = int(input(f"Masukkan jumlah baru untuk {keranjang[idx]['nama']}: "))
                    if qty_baru <= 0:
                        print("Jumlah harus lebih dari 0.")
                        continue
                    keranjang[idx]['qty'] = qty_baru
                    print("Jumlah berhasil diubah.\n")
                    break
                except ValueError:
                    print("Jumlah harus angka!\n")
        else:
            print("Nomor item tidak valid.\n")
    except ValueError:
        print("Input harus angka!\n")

# ======== Checkout ========
def checkout():
    lihat_keranjang()
    if not keranjang:
        return
    konfirmasi = input("Lanjutkan ke checkout? (y/n): ").lower()
    if konfirmasi == "y":
        print("Checkout berhasil! Terima kasih telah berbelanja.\n")
        keranjang.clear()
    else:
        print("Checkout dibatalkan.\n")

# ======== Menu Utama User ========
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
            lihat_keranjang()
        elif pilihan == "4":
            hapus_keranjang()
        elif pilihan == "5":
            ubah_jumlah_keranjang()
        elif pilihan == "6":
            checkout()
        elif pilihan == "7":
            print("Sampai jumpa, semoga harimu menyenangkan!")
            break
        else:
            print("Pilihan tidak valid.\n")

# ======== Jalankan Program ========
main_menu()
