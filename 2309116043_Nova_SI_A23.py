# import fungsi matematika python
import math

# sebuah variable pengguna yang berisi value username dan password
list_pengguna = {"nova": "1234", "nova2": "1233"}


# Fungsi untuk melakukan proses login
def login():
    # sebuah variable inputan
    username = input("Masukkan nama pengguna: ")
    password = input("Masukkan kata sandi: ")

    # Periksa apakah nama pengguna ada dalam database
    # percabangan if yang memiliki parameter untuk mencocokan username dan password yang berada dalam list (list_pengguna)

    if username in list_pengguna and list_pengguna[username] == password:
        print("Login berhasil! Selamat datang,", username)
        print("\n")

        print("kakulator menghitung segitiga pythagoras.")
        print("1. alas")
        print("2. segi tegak")
        print("3. sisi miring")
        # memanggil def kalkulator
        kalkulator_phytagoras()
    else:
        print("Login gagal. Nama pengguna atau kata sandi salah.")


# fungsi def (definition) yang di beri nama kalkulator
def kalkulator_phytagoras():
    # variable pilihan untuk menyimpan value inputan menu
    pilihan = int(input("Masukkan pilihan (1-3): "))

    # sebuah fungsi percabangan if else untuk menu yang didalam setiap menunya menyimpan perhitungan kalkulator sederhana

    # menu pertama untuk penjumlahan dengan value hasil perhitungan disimpan di dalam variable hasil
    if pilihan == 1:
        # ini adalah inputan untuk sisi miring dan tegak
        sisi_miring = int(input("Masukkan angka sisi miring: "))
        sisi_tegak = int(input("Masukkan angka sisi tegak  : "))

        # ini adalah variable untuk menghitung alas segitiga phytagoras
        alas = math.sqrt(sisi_miring**2 - sisi_tegak**2)
        print("Hasil Perhitungan alas adalah : ", alas)
    # menu pertama untuk pengurangan dengan value hasil perhitungan disimpan di dalam variable hasil

    elif pilihan == 2:
        sisi_miring = int(input("Masukkan angka sisi miring: "))
        alas = int(input("Masukkan angka alas  : "))
        sisi_tegak = math.sqrt(sisi_miring**2 - alas**2)
        print("Hasil Perhitungan alas adalah : ", sisi_tegak)

    # menu pertama untuk perkalian dengan value hasil perhitungan disimpan di dalam variable hasil
    elif pilihan == 3:
        sisi_tegak = int(input("Masukkan angka sisi miring: "))
        alas = int(input("Masukkan angka alas  : "))
        sisi_miring = math.sqrt(alas**2 + sisi_tegak**2)
        print("Hasil Perhitungan sisi miring adalah : ", sisi_miring)

    # ketika semua pilihan tidak ada
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    print("=======================================")

    # menampilkan hasil perhitungan yang diambil dari value hasil


# Memanggil fungsi login
kalkulator_phytagoras()
login()
