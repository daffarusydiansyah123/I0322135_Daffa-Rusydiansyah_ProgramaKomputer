#Soal No 1
class Anggota:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.saldo = 0

    def setor_sampah(self, berat):
        nilai = berat * HargaSampah.get_harga()
        self.saldo += nilai
        Transaksi.tambah_transaksi(self.nama, 'Setor Sampah', berat, nilai)

    def tarik_saldo(self, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            Transaksi.tambah_transaksi(self.nama, 'Tarik Saldo', 0, -jumlah)
        else:
            print("Saldo tidak mencukupi.")

    def __str__(self):
        return f"Nama: {self.nama}\nAlamat: {self.alamat}\nSaldo: {self.saldo}"


class HargaSampah:
    harga = 0

    @staticmethod
    def set_harga(harga):
        HargaSampah.harga = harga

    @staticmethod
    def get_harga():
        return HargaSampah.harga


class Transaksi:
    transaksi = []

    @staticmethod
    def tambah_transaksi(nama, jenis, berat, nilai):
        Transaksi.transaksi.append({
            'Nama': nama,
            'Jenis': jenis,
            'Berat': berat,
            'Nilai': nilai
        })

    @staticmethod
    def tampilkan_transaksi():
        for transaksi in Transaksi.transaksi:
            print(transaksi)


# Inisialisasi harga sampah
HargaSampah.set_harga(500)  # Misalnya, harga sampah Rp500 per kilogram

# Membuat objek anggota
anggota1 = Anggota("John Doe", "Jl. Anggrek No. 123")
anggota2 = Anggota("Jane Smith", "Jl. Mawar No. 456")

# Setoran sampah oleh anggota
anggota1.setor_sampah(5)  # John Doe menyetor 5 kg sampah
anggota2.setor_sampah(3)  # Jane Smith menyetor 3 kg sampah

# Menampilkan saldo anggota
print(anggota1)
print("\n")
print(anggota2)
print("\n")

# Menampilkan transaksi
Transaksi.tampilkan_transaksi()

#soal No 2
import json

def tambah_anggota(nama, alamat, telepon):
    with open("anggotas.json", "r+") as file:
        data = json.load(file)
        id_anggota = str(len(data) + 1).zfill(5)
        
        new_anggota = {
            "idanggota": id_anggota,
            "nama": nama,
            "alamat": alamat,
            "tanggal": "2023-04-03",
            "telepon": telepon
        }
        
        data[id_anggota] = new_anggota
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    
    print("Berhasil menambahkan data anggota.")
    input("Tekan enter untuk melanjutkan...")

# Contoh penggunaan fungsi
nama = input("Nama: ")
alamat = input("Alamat: ")
telepon = input("Nomor Telepon: ")

tambah_anggota(nama, alamat, telepon)
#2B
import json

def cari_anggota_by_id(id_anggota):
    with open("anggotas.json", "r") as file:
        data = json.load(file)
        
        if id_anggota in data:
            anggota = data[id_anggota]
            return anggota
        
    return {}

# Contoh penggunaan fungsi
id_anggota = input("Masukkan ID Anggota: ")

hasil_cari = cari_anggota_by_id(id_anggota)

if hasil_cari:
    print("Data Anggota:")
    print(hasil_cari)
else:
    print("Data anggota tidak ditemukan.")

#2C
def tampilkan_anggota(anggota):
    if anggota:
        print("ID Anggota :", anggota["idanggota"])
        print("Nama :", anggota["nama"])
        print("Alamat :", anggota["alamat"])
        print("Telepon :", anggota["telepon"])
        print("Tanggal Daftar :", anggota["tanggal"])
    else:
        print("Tidak ada data anggota!")

# Contoh penggunaan fungsi
id_anggota = input("Masukkan ID Anggota: ")

hasil_cari = cari_anggota_by_id(id_anggota)

tampilkan_anggota(hasil_cari)

#no 2D
import os
import json

def edit_anggota():
    while True:
        id_anggota = input("Ketik ID anggota yang akan diedit: ")
        anggota = cari_anggota_by_id(id_anggota)
        
        if anggota:
            print("Nama:", anggota["nama"])
            nama = input("Nama: ")
            if nama:
                anggota["nama"] = nama
            
            print("Alamat:", anggota["alamat"])
            alamat = input("Alamat: ")
            if alamat:
                anggota["alamat"] = alamat
            
            print("Telepon:", anggota["telepon"])
            telepon = input("Telepon: ")
            if telepon:
                anggota["telepon"] = telepon
            
            with open("anggotas.json", "r+") as file:
                data = json.load(file)
                data[id_anggota] = anggota
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
            
            print("Data berhasil diubah.")
            break
        else:
            pilihan = input("Data anggota tidak ditemukan!\nCari lagi (Y/y = Ya, T/t = Tidak)? ")
            if pilihan.lower() != "y":
                break
            os.system("cls" if os.name == "nt" else "clear")

# Contoh penggunaan fungsi
edit_anggota()

#Soal No3
import anggota

def tampilkan_menu():
    print("===============================")
    print("** Program Pengelolaan Tabungan Sampah **")
    print("===============================")
    print("Pilihan menu:")
    print("1. Pengelolaan Keanggotaan")
    print("   1a. Penambahan Data Anggota")
    print("   1b. Pencarian Data Anggota")
    print("   1c. Pengubahan Data Anggota")
    print("9. Exit")

def penambahan_data_anggota():
    print("Penambahan data anggota.")
    nama = input("Nama: ")
    alamat = input("Alamat: ")
    telepon = input("Nomor Telepon: ")

    anggota.tambah_anggota(nama, alamat, telepon)
    input("Tekan Enter untuk melanjutkan...")

def pencarian_data_anggota():
    # Implementasikan fungsi pencarian data anggota di sini
    pass

def pengubahan_data_anggota():
    # Implementasikan fungsi pengubahan data anggota di sini
    pass

# Program Utama
while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1a":
        penambahan_data_anggota()
    elif pilihan == "1b":
        pencarian_data_anggota()
    elif pilihan == "1c":
        pengubahan_data_anggota()
    elif pilihan == "9":
        print("Terima kasih")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
        input("Tekan Enter untuk melanjutkan...")

#soal No 4








