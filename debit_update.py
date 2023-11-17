def menu_makanan():
    print("----------------------------------------")
    print("|   SELAMAT DATANG DI FEAST OF JAPAN   |")
    print("----------------------------------------")
    print("|===============================|")
    print("|          MENU MAKANAN         |")
    print("| 1. Sushi           Rp. 100000 |")
    print("| 2. Ramen           Rp. 60000  |")
    print("| 3. Udon            Rp. 50000  |")
    print("| 4. Sashimi         Rp. 90000  |")
    print("| 5. Takoyaki        Rp. 70000  |")
    print("|===============================|")

    menu_makanan_0113 = int(input("Pilih Menu Makanan (1/2/3/4/5): "))

    if menu_makanan_0113 not in range(1, 6):
        print("Maaf menu ini tidak tersedia")
        return None

    jumlah_porsi_makanan_0113 = int(input("Jumlah Porsi : "))
    harga_makanan = [100000, 60000, 50000, 90000, 70000]
    total_makanan_0113 = jumlah_porsi_makanan_0113 * harga_makanan[menu_makanan_0113 - 1]
    nama_makanan_0113 = ["Sushi", "Ramen", "Udon", "Sashimi", "Takoyaki"][menu_makanan_0113 - 1]

    print(f"{nama_makanan_0113} {jumlah_porsi_makanan_0113} Jumlah Porsi: Rp {total_makanan_0113}")
    print(f"Total Harga Makanan : Rp {total_makanan_0113}")
    return nama_makanan_0113, jumlah_porsi_makanan_0113, total_makanan_0113


def menu_tambahan():
    print("|====================================|")
    print("|     MENU MINUMAN NON ALKOHOL       |")
    print("|  1. Matcha Latte       Rp. 45000   |")
    print("|  2. Milk Tea           Rp. 35000   |")
    print("|  3. Ofukucha           Rp. 40000   |")
    print("|  4. Thai Tea           Rp. 25000   |")
    print("|  5. Teh Sakura         Rp. 30000   |")
    print("|====================================|")
    print("|     MENU MINUMAN (ALKOHOL)         |")
    print("|  6. Beer               Rp. 50000   |")
    print("|  7. Wine               Rp. 250000  |")
    print("|  8. Whiskey            Rp. 200000  |")
    print("|  9. Shochu             Rp. 100000  |")
    print("|  10. Sake              Rp. 150000  |")
    print("|=====================================")

    menu_tambahan_0113 = int(input("Pilih Menu Minuman  Non Alkohol (1/2/3/4/5) Alkohol (6/7/8/9/10): "))

    if menu_tambahan_0113 not in range(1, 11):
        print("Maaf menu ini tidak tersedia")
        return None

    jumlah_porsi_tambahan_0113 = int(input("Jumlah Porsi : "))
    harga_tambahan = [ 45000, 35000, 40000, 25000, 30000, 50000, 250000, 200000, 100000, 150000][menu_tambahan_0113 - 1]
    total_tambahan_0113 = jumlah_porsi_tambahan_0113 * harga_tambahan
    nama_tambahan_0113 = ["Matcha Latte", "Milk Tea", "Ofukucha", "Thai Tea","Teh Sakura", "Beer", "Wine", "Whiskey", "Shochu", "Sake"][menu_tambahan_0113 - 1]

    print(f"{nama_tambahan_0113} {jumlah_porsi_tambahan_0113} Jumlah Porsi: Rp {total_tambahan_0113}")
    print(f"Total Harga Tambahan : Rp {total_tambahan_0113}")
    return nama_tambahan_0113, jumlah_porsi_tambahan_0113, total_tambahan_0113


def pesanan_restoran():
    total_pesanan = 0
    makanan_pesanan = menu_makanan()
    minuman_pesanan = menu_tambahan()
    nim = input("Masukkan Nim Anda :")
    nama = input("Masukkan Nama Anda: ")

    if makanan_pesanan is not None and minuman_pesanan is not None:
        total_pesanan += makanan_pesanan[2] + minuman_pesanan[2]
        print("\nTotal Pesanan Anda : ")
        print(f"{makanan_pesanan[0]} x {makanan_pesanan[1]}")
        print(f"{minuman_pesanan[0]} x {minuman_pesanan[1]}")
        print(f"Total Pembayaran : Rp {total_pesanan}")
        nominal_pembayaran = float(input("Masukkan Nominal Pembayaran: "))
        kembalian = nominal_pembayaran - total_pesanan
        print("\n===== STRUK PEMBAYARAN =====")
        print(f"NIM: {nim}")
        print(f"Nama: {nama}")
        print(f"Total Akhir: Rp. {total_pesanan}")
        print(f"Nominal Pembayaran: Rp. {nominal_pembayaran}")
        print(f"Kembalian: Rp. {kembalian}")
        print("==========================================")
        print(" Terima kasih telah berbelanja di FEAST OF JAPAN.")
        print(" Sampai jumpa lain kali.")
        print("==========================================")
    elif makanan_pesanan is not None:
        total_pesanan += makanan_pesanan[2]
        print("\nTotal Pesanan Anda : ")
        print(f"{makanan_pesanan[0]} x {makanan_pesanan[1]}")
        print(f"Total Pembayaran : Rp {total_pesanan}")
        nominal_pembayaran = float(input("Masukkan Nominal Pembayaran: "))
        kembalian = nominal_pembayaran - total_pesanan
        print("\n=========== STRUK PEMBAYARAN ===========")
        print(f"NIM: {nim}")
        print(f"Nama: {nama}")
        print(f"Total Akhir: Rp. {total_pesanan}")
        print(f"Nominal Pembayaran: Rp. {nominal_pembayaran}")
        print(f"Kembalian: Rp. {kembalian}")
        print("==========================================")
        print(" Terima kasih telah berbelanja di FEAST OF JAPAN.")
        print(" Sampai jumpa lain kali.")
        print("==========================================")
    elif minuman_pesanan is not None:
        total_pesanan += minuman_pesanan[2]
        print("\nTotal Pesanan Anda : ")
        print(f"{minuman_pesanan[0]} x {minuman_pesanan[1]}")
        print(f"Total Pembayaran : Rp {total_pesanan}")
        nominal_pembayaran = float(input("Masukkan Nominal Pembayaran: "))
        kembalian = nominal_pembayaran - total_pesanan
        print("\n===== STRUK PEMBAYARAN =====")
        print(f"NIM: {nim}")
        print(f"Nama: {nama}")
        print(f"Total Akhir: Rp. {total_pesanan}")
        print(f"Nominal Pembayaran: Rp. {nominal_pembayaran}")
        print(f"Kembalian: Rp. {kembalian}")
        print("==========================================")
        print(" Terima kasih telah berbelanja di FEAST OF JAPAN.")
        print(" Sampai jumpa lain kali.")
        print("==========================================")

pesanan_restoran()
