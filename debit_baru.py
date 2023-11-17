
def menu_makanan():
    print("\n== Menu Makanan ==")
    print("|=====================================")
    print("|  1. Mie Ayam              Rp. 20000 |")
    print("|  2. Ramen                 Rp. 25000 |")
    print("|  3. Bubur Ayam            Rp. 20000 |")
    print("|  4. Nasi Goreng           Rp. 25000 |")
    print("|  5. Pecel Lele            Rp. 20000 |")
    print("|=====================================")

    menu_makanan_0113 = int(input("Pilih Menu Makanan (1/2/3/4/5): "))

    if menu_makanan_0113 not in range(1, 6):
        print("Maaf menu ini tidak tersedia")
        return None

    jumlah_porsi_makanan_0113 = int(input("Jumlah Porsi : "))
    harga_makanan = [20000, 25000, 20000, 25000, 20000]
    total_makanan_0113 = jumlah_porsi_makanan_0113 * harga_makanan[menu_makanan_0113 - 1]
    nama_makanan_0113 = ["Mie Ayam", "Ramen", "Bubur Ayam", "Nasi Goreng", "Pecel Lele"][menu_makanan_0113 - 1]

    print(f"{nama_makanan_0113} {jumlah_porsi_makanan_0113} Jumlah Porsi: Rp {total_makanan_0113}")
    print(f"Total Harga Makanan : Rp {total_makanan_0113}")
    return nama_makanan_0113, jumlah_porsi_makanan_0113

def menu_tambahan():
    print("\n== Menu Minuman ==")
    print("|=====================================")
    print("|  1. Es Teh             Rp. 5000 |")
    print("|  2. Coca-Cola          Rp. 8000 |")
    print("|  3. Orange Juice       Rp. 10000 |")
    print("|  4. Pisang Ambon       Rp. 12000 |")
    print("|  5. Susu               Rp. 6000 |")
    print("|=====================================")
    print("\n== Menu Minuman Alkohol ==")
    print("|=====================================")
    print("|  6. Beer              Rp. 60000 |")
    print("|  7. Wine              Rp. 250000 |")
    print("|  8. Whiskey           Rp. 200000 |")
    print("|  9. Shochu            Rp. 100000 |")
    print("|  10. Sake             Rp. 150000 |")
    print("|=====================================")

    menu_tambahan_0113 = int(input("Pilih Menu Minuman Alkohol (6/7/8/9/10) Non Alkohol (1/2/3/4/5) : "))

    if menu_tambahan_0113 not in range(1, 11):
        print("Maaf menu ini tidak tersedia")
        return None

    jumlah_porsi_tambahan_0113 = int(input("Jumlah Porsi : "))
    harga_tambahan = [60000, 250000, 200000, 100000, 150000, 5000, 8000, 10000, 12000, 6000][menu_tambahan_0113 - 1]
    total_tambahan_0113 = jumlah_porsi_tambahan_0113 * harga_tambahan
    nama_tambahan_0113 = ["Beer", "Wine", "Whiskey", "Shochu", "Sake", "Es Teh", "Coca-Cola", "Orange Juice", "Pisang Ambon", "Susu"][menu_tambahan_0113 - 1]

    print(f"{nama_tambahan_0113} {jumlah_porsi_tambahan_0113} Jumlah Porsi: Rp {total_tambahan_0113}")
    print(f"Total Harga Tambahan : Rp {total_tambahan_0113}")
    return nama_tambahan_0113, jumlah_porsi_tambahan_0113

def pesanan_restoran():
    makanan_pesanan = menu_makanan()
    minuman_pesanan = menu_tambahan()

    if makanan_pesanan is not None and minuman_pesanan is not None:
        print("\nTotal Pesanan Anda : ")
        print(f"{makanan_pesanan[0]} x {makanan_pesanan[1]}")
        print(f"{minuman_pesanan[0]} x {minuman_pesanan[1]}")
        print("==========================================")
        print(" Terima kasih telah berbelanja di restoran kami.")
        print(" Sampai jumpa lain kali.")
        print("==========================================")
    elif makanan_pesanan is not None:
        print("\nTotal Pesanan Anda : ")
        print(f"{makanan_pesanan[0]} x {makanan_pesanan[1]}")
        print("==========================================")
        print(" Terima kasih telah berbelanja di restoran kami.")
        print(" Sampai jumpa lain kali.")
        print("==========================================")
    elif minuman_pesanan is not None:
        print("\nTotal Pesanan Anda : ")
        print(f"{minuman_pesanan[0]} x {minuman_pesanan[1]}")
        print("==========================================")
        print(" Terima kasih telah berbelanja di restoran kami.")
        print(" Sampai jumpa lain kali.")
        print("==========================================")

pesanan_restoran()