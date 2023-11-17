def menu_makanan():
    print("|================================|")
    print("|     MENU MAKANAN (MASAKAN)     |")
    print("|  1. Ramen            Rp. 20000 |")
    print("|  2. Sushi            Rp. 40000 |")
    print("|  3. Katsudon         Rp. 30000 |")
    print("|  4. Sashimi          Rp. 50000 |")
    print("|  5. Yakisoba         Rp. 25000 |")
    print("|================================|")

    menu_makanan_0113 = int(input("Pilih Menu Makanan (1/2/3/4/5) : "))

    if menu_makanan_0113 not in range(1, 11):
        print("Maaf menu ini tidak tersedia")
        return None

    jumlah_porsi_makanan_0113 = int(input("Jumlah Porsi : "))
    harga_makanan = [20000, 40000, 30000, 50000, 25000]
    total_makanan_0113 = jumlah_porsi_makanan_0113 * harga_makanan[menu_makanan_0113 - 1]
    nama_makanan_0113 = ["Ramen", "Sushi", "Katsudon", "Sashimi", "Yakisoba"][menu_makanan_0113 - 1]

    print(f"{nama_makanan_0113} {jumlah_porsi_makanan_0113} Jumlah Porsi: Rp {total_makanan_0113}")
    print(f"Total Harga Makanan : Rp {total_makanan_0113}")
    return nama_makanan_0113, jumlah_porsi_makanan_0113


def menu_tambahan():
    print("|====================================|")
    print("|     MENU MINUMAN (NON ALKOHOL)     |")
    print("|  1. Es Teh             Rp. 5000    |")
    print("|  2. Coca-Cola          Rp. 8000    |")
    print("|  3. Orange Juice       Rp. 10000   |")
    print("|  4. Pisang Ambon       Rp. 12000   |")
    print("|  5. Susu               Rp. 6000    |")
    print("|     MENU MINUMAN (ALKOHOL)         |")
    print("|  6. Beer               Rp. 50000   |")
    print("|  7. Wine               Rp. 250000  |")
    print("|  8. Whiskey            Rp. 200000  |")
    print("|  9. Shochu             Rp. 100000  |")
    print("|  10. Sake              Rp. 150000  |")
    print("|=====================================")

    menu_tambahan_0113 = int(input("Pilih Menu Minuman Alkohol (1/2/3/4/5) Non Alkohol (6/7/8/9/10): "))

    if menu_tambahan_0113 not in range(1, 11):
        print("Maaf menu ini tidak tersedia")
        return None

    jumlah_porsi_tambahan_0113 = int(input("Jumlah Porsi : "))
    harga_tambahan = [5000, 8000, 10000, 12000, 6000, 50000, 250000, 200000, 100000, 150000]
    total_tambahan_0113 = jumlah_porsi_tambahan_0113 * harga_tambahan[menu_tambahan_0113 - 1]
    nama_tambahan_0113 = ["Es Teh", "Coca-Cola", "Orange Juice", "Pisang Ambon", "Susu" ,"Beer", "Wine", "Whiskey", "Shochu", "Sake"][menu_tambahan_0113 - 1]

    print(f"{nama_tambahan_0113} {jumlah_porsi_tambahan_0113} Jumlah Porsi: Rp {total_tambahan_0113}")
    print(f"Total Harga Minuman : Rp {total_tambahan_0113}")
    return nama_tambahan_0113, jumlah_porsi_tambahan_0113


def kembalian():
    total_pembelian = total_makanan_0113 + total_tambahan_0113
    print(f"total pembelian : {total_pembelian}")
    bayaran = int(input("Bayaran: Rp "))
    if bayaran >= total_pembelian:
        kembalian_pembayaran = bayaran - total_pembelian
        print(f"Total Pembelian : Rp {total_pembelian}")
        print(f"Kembalian Anda : Rp {kembalian_pembayaran}")
    else:
        print("Maaf bayaran Anda tidak mencukupi, silahkan ulangi")
        kembalian()

nim = input("Nim anda:")
nama = input("Nama anda: ")
nama_makanan, jumlah_porsi_makanan = menu_makanan()
nama_tambahan, jumlah_porsi_tambahan = menu_tambahan()
total_makanan_0113 = jumlah_porsi_makanan * 20000
total_tambahan_0113 = jumlah_porsi_tambahan * 5000


print("\n===STRUK PEmBAYARAN===")
print("Nim :", nim)
print("Nama :", nama)
print(f"1. {nama_makanan} {jumlah_porsi_makanan} Porsi")
print(f"2. {nama_tambahan} {jumlah_porsi_tambahan} Porsi")

kembalian()
