import math

# === DEFINISI FUNGSI ===
def proses_luas_persegi(sisi):
    return sisi * sisi

def proses_keliling_persegi(sisi):
    return 4 * sisi

def cek_status_prima(bilangan):
    if bilangan <= 1:
        return False
    for i in range(2, int(math.isqrt(bilangan)) + 1):
        if bilangan % i == 0:
            return False
    return True

def cek_paritas_bilangan(bilangan):
    if bilangan % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def proses_luas_lingkaran(r):
    return 3.14 * r * r

def proses_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi


# === TAMPILAN MENU UTAMA ===
while True:
    print("\n==========================================")
    print("     KALKULATOR & LOGIKA NUMERIK          ")
    print("==========================================")
    print("1. Hitung Luas Persegi")
    print("2. Hitung Keliling Persegi")
    print("3. Cek Bilangan Prima")
    print("4. Cek Bilangan Genap / Ganjil")
    print("5. Hitung Luas Lingkaran")
    print("6. Hitung Luas Segitiga")
    print("7. Keluar")
    print("==========================================")
    
    pilihan_user = input("Pilih menu (1-7): ")
    
    if pilihan_user == "1":
        nilai_sisi = float(input("Masukkan panjang sisi: "))
        print(f"Hasil Luas Persegi = {proses_luas_persegi(nilai_sisi)}")
        
    elif pilihan_user == "2":
        nilai_sisi = float(input("Masukkan panjang sisi: "))
        print(f"Hasil Keliling Persegi = {proses_keliling_persegi(nilai_sisi)}")
        
    elif pilihan_user == "3":
        input_angka = int(input("Masukkan angka: "))
        if cek_status_prima(input_angka):
            print(f"Angka {input_angka} termasuk Bilangan Prima.")
        else:
            print(f"Angka {input_angka} BUKAN Bilangan Prima.")
            
    elif pilihan_user == "4":
        input_angka = int(input("Masukkan angka: "))
        print(f"Angka {input_angka} adalah Bilangan {cek_paritas_bilangan(input_angka)}.")
            
    elif pilihan_user == "5":
        nilai_r = float(input("Masukkan jari-jari: "))
        print(f"Hasil Luas Lingkaran = {proses_luas_lingkaran(nilai_r)}")

    elif pilihan_user == "6":
        nilai_alas = float(input("Masukkan alas: "))
        nilai_tinggi = float(input("Masukkan tinggi: "))
        print(f"Hasil Luas Segitiga = {proses_luas_segitiga(nilai_alas, nilai_tinggi)}")
        
    elif pilihan_user == "7":
        print("Program dihentikan, terima kasih!")
        break
    else:
        print("Menu tidak valid! Silakan masukkan angka 1-7.")
