data_pengeluaran = []

def tampilkan_menu():
    print("\n===CATATAN PENGELUARAN===")
    print("1. Tambah Pengeluaran")
    print("2. Lihat Semua Pengeluaran")
    print("3. Lihat Total Pengeluaran")
    print("4. Keluar")
    return input("Pilih Menu [1-4]: ")

def tambah_pengeluaran():
    name = input("Masukkan Nama Pengeluaran: ")
    try:
        jumlah = int(input("Masukkan Jumlah Rp:"))
        data_pengeluaran.append({"nama": name, "jumlah": jumlah})
        print(f"Berhasil ditambah: {name} Rp {jumlah}")
    except ValueError:
        print("Jumlah harus angka ya!")

def lihat_pengeluaran():
    if not data_pengeluaran:
        print("Belum ada pengeluaran----")
        return

    print("\n---Daftar Pengeluaran ---")
    total = 0
    for i, item in enumerate(data_pengeluaran, 1):
        print(f"{i}. {item['nama']} : Rp {item['jumlah']}")
        total += item['jumlah']
    print(f"Total: Rp {total}")

def simpan_ke_file():
    with open("pengeluaran.txt", "w") as f:
        for item in data_pengeluaran:
            f.write(f"{item['nama']}, {item['jumlah']}\n")
    print("Data tersimpan ke pengeluaran.txt")

while True:
    pilihan = tampilkan_menu()

    if pilihan == "1":
        tambah_pengeluaran()
    elif pilihan == "2":
        lihat_pengeluaran()
    elif pilihan == "3":
        lihat_pengeluaran()
    elif pilihan == "4":
        simpan_ke_file()

        print("Terimaksih sudah pakai program ini!")
        break
    else:
        print("Pilihan tidak ada. Coba lagi!")
