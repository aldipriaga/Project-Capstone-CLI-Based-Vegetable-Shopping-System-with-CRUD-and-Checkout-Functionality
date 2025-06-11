# ===== Data Produk (CREATE) =====
produk_dict = {
    1: {"nama": "Tomat", "kategori": "Buah", "berat": 500, "harga": 8000},
    2: {"nama": "Cabai rawit Merah", "kategori": "Sayur", "berat": 150, "harga": 30000},
    3: {"nama": "Cabai keriting Merah", "kategori": "Sayur", "berat": 150, "harga": 25000},
    4: {"nama": "Bawang Merah", "kategori": "Sayur", "berat": 250, "harga": 17900},
    5: {"nama": "Bawang Putih", "kategori": "Sayur", "berat": 250, "harga": 16000},
    6: {"nama": "Bawang bombay", "kategori": "Sayur", "berat": 400, "harga": 36000},
    7: {"nama": "Buncis", "kategori": "Sayur", "berat": 200, "harga": 7500},
    8: {"nama": "Pakcoy", "kategori": "Sayur", "berat": 150, "harga": 4900},
    9: {"nama": "Wortel", "kategori": "Sayur", "berat": 500, "harga": 15400},
    10: {"nama": "Kangkung", "kategori": "Sayur", "berat": 200, "harga": 5300},
    11: {"nama": "Terong ungu", "kategori": "Sayur", "berat": 450, "harga": 9000},
    12: {"nama": "Timun", "kategori": "Buah", "berat": 500, "harga": 10800},
    13: {"nama": "Kol", "kategori": "Sayur", "berat": 1000, "harga": 23800},
    14: {"nama": "Sawi putih", "kategori": "Sayur", "berat": 600, "harga": 1200},
    15: {"nama": "Melon", "kategori": "Buah", "berat": 1500, "harga": 44000},
    16: {"nama": "Semangka", "kategori": "Buah", "berat": 3000, "harga": 44500},
    17: {"nama": "Jeruk Lemon", "kategori": "Buah", "berat": 500, "harga": 25000},
    18: {"nama": "Anggur", "kategori": "Buah", "berat": 500, "harga": 43000},
    19: {"nama": "Nanas", "kategori": "Buah", "berat": 1000, "harga": 18900},
    20: {"nama": "Mangga Super", "kategori": "Buah", "berat": 1000, "harga": 53100},
}

# ====== Data Keranjang Belanja (READ / UPDATE / DELETE) ======
keranjang = {}

# Fungsi input angka agar aman
def input_int(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input must be a number!")

# Format angka ke Rupiah
def format_rupiah(angka):
    return f"Rp{angka:,}".replace(",", ".")

# ===== CRUD Produk =====

# Menampilkan semua kategori produk
def tampilkan_kategori():
    kategori_list = list(set(prod['kategori'] for prod in produk_dict.values()))
    for i, kategori in enumerate(kategori_list, 1):
        print(f"{i}. {kategori}")
    return kategori_list

# Menampilkan semua produk dalam kategori tertentu
def tampilkan_produk_per_kategori(kategori):
    produk_kategori = {pid: info for pid, info in produk_dict.items() if info['kategori'] == kategori}
    for pid, info in produk_kategori.items():
        print(f"{pid}. {info['nama']} - {info['berat']}gr - {format_rupiah(info['harga'])}")
    return produk_kategori

# Fitur lihat produk tanpa harus belanja (READ)
def lihat_produk():
    while True:
        print("\n=== VIEW PRODUCTS ===")
        kategori_list = tampilkan_kategori()
        print("0. Back")

        pilihan = input_int("Choose category (number): ")
        if pilihan == 0:
            break
        if 1 <= pilihan <= len(kategori_list):
            kategori = kategori_list[pilihan - 1]
            tampilkan_produk_per_kategori(kategori)
        else:
            print("Invalid category.")

# Menampilkan isi keranjang (READ)
def tampilkan_keranjang():
    if not keranjang:
        print("\nCart is empty.")
        return 0, 0

    print("\n=== SHOPPING CART ===")
    total, total_berat = 0, 0
    for i, (nama, item) in enumerate(keranjang.items(), 1):
        subtotal = item['qty'] * item['harga']
        berat = item['qty'] * item['berat']
        total += subtotal
        total_berat += berat
        print(f"{i}. {nama} x{item['qty']} - {berat}gr - {format_rupiah(subtotal)}")

    print(f"Total Weight : {total_berat}gr")
    print(f"Total Price  : {format_rupiah(total)}")
    return total, total_berat

# ===== CRUD Keranjang =====

# CREATE - Tambah ke keranjang
def tambah_ke_keranjang():
    while True:
        print("\n=== SELECT CATEGORY ===")
        kategori_list = tampilkan_kategori()
        print("0. Back")

        pilihan = input_int("Choose category (number): ")
        if pilihan == 0:
            break
        if not (1 <= pilihan <= len(kategori_list)):
            print("Invalid category.")
            continue

        kategori_terpilih = kategori_list[pilihan - 1]
        produk_kategori = tampilkan_produk_per_kategori(kategori_terpilih)

        while True:
            print("0. Back to category")
            id_produk = input_int("Enter Product ID to purchase: ")
            if id_produk == 0:
                break

            produk = produk_kategori.get(id_produk)
            if not produk:
                print("Product not found.")
                continue

            qty = input_int("Enter quantity: ")
            if qty <= 0:
                print("Quantity must be more than 0.")
                continue
            nama = produk['nama']
            if nama in keranjang:
                keranjang[nama]['qty'] += qty
            else:
                keranjang[nama] = {"harga": produk['harga'], "qty": qty, "berat": produk['berat']}
            print(f"{nama} has been added to cart.")

# UPDATE - Ubah jumlah item di keranjang
def ubah_keranjang():
    while keranjang:
        tampilkan_keranjang()
        print("0. Back")
        idx = input_int("Choose item number to update: ")
        if idx == 0:
            break
        nama_list = list(keranjang)
        if not (1 <= idx <= len(nama_list)):
            print("Invalid item number.")
            continue
        nama = nama_list[idx - 1]
        qty_baru = input_int(f"Enter new quantity for {nama}: ")
        if qty_baru > 0:
            keranjang[nama]['qty'] = qty_baru
            print("Quantity updated successfully.")
        else:
            print("Quantity must be more than 0.")

# DELETE - Hapus item dari keranjang
def hapus_keranjang():
    while keranjang:
        tampilkan_keranjang()
        print("0. Back")
        idx = input_int("Choose item number to delete: ")
        if idx == 0:
            break
        nama_list = list(keranjang)
        if not (1 <= idx <= len(nama_list)):
            print("Invalid item number.")
            continue
        nama = nama_list[idx - 1]
        if input(f"Delete {nama}? (y/n): ").lower() == "y":
            del keranjang[nama]
            print("Item deleted.")

# Checkout - tampilkan total belanja
def checkout():
    total, total_berat = tampilkan_keranjang()
    if total == 0:
        return
    if input("Proceed to checkout? (y/n): ").lower() == "y":
        print("\n=== RECEIPT ===")
        print(f"Total Weight : {total_berat}gr")
        print(f"Total Price  : {format_rupiah(total)}")
        print("Thank you for shopping with us!")
        keranjang.clear()

# ===== MAIN PROGRAM =====

def main():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. View Products")       # READ
        print("2. Add to Cart")        # CREATE
        print("3. View Cart")          # READ
        print("4. Update Cart")        # UPDATE
        print("5. Remove from Cart")   # DELETE
        print("6. Checkout")           
        print("7. Exit")

        pilihan = input("Choose menu (1-7): ")
        if pilihan == "1":
            lihat_produk()
        elif pilihan == "2":
            tambah_ke_keranjang()
        elif pilihan == "3":
            tampilkan_keranjang()
        elif pilihan == "4":
            ubah_keranjang()
        elif pilihan == "5":
            hapus_keranjang()
        elif pilihan == "6":
            checkout()
        elif pilihan == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
