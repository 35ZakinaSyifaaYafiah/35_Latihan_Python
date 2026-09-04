# Meminta input angka dari pengguna
angka = int(input("Masukkan sebuah angka: "))

# Mengecek sisa bagi dengan 2
if angka % 2 == 0:
    print(f"Angka {angka} adalah bilangan genap.")
else:
    print(f"Angka {angka} adalah bilangan ganjil.")
# Inisialisasi variabel untuk mengontrol perulangan
    lanjut = "y"
    
    # Perulangan akan terus berjalan selama variabel lanjut bernilai 'y' atau 'Y'
    while lanjut.lower() == "y":
        # 1. Input bilangan dari pengguna
        bilangan = int(input("\nMasukkan sebuah bilangan: "))
    
        # 2. Logika Modulus (sisa pembagian dengan 2)
        if bilangan % 2 == 0:
            print(f"--> {bilangan} adalah bilangan GENAP")
        else:
            print(f"--> {bilangan} adalah bilangan GANJIL")
    
        # 3. Menanyakan apakah pengguna ingin mengulang atau keluar
        lanjut = input(
            "\nApakah ingin mengecek bilangan lain? (y/n untuk keluar): "
        )
    
    print("\nProgram selesai. Terima kasih telah menggunakan program ini!")
    
    
    #Modul ganjilgenap
def ganjil_genap(a):
    while True:
        ank = int(input("angkamu = "))
        if ank % 2 == 0:
            print(f"{ank} adalah bilangan GENAP")
        else:
            print(f"{ank} adalah bilangan GANJIL")
            
        # Hentikan program jika pengguna mengetik 'stop'    
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")   
        
        if pilihan == 'stop':
            print("Program selesai.")
            break
                

#Modul Pembagian
def pembagian(c):
    while True:
        angka = int(input("angkamu = "))
        ank = int(input("dibagi dengan angka = "))
        print(f"{angka} / {ank} = {angka / ank}")
        
        # Hentikan program jika pengguna mengetik 'stop'    
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")   
                
        if pilihan == 'stop':
            print("Program selesai.")
            break
        
       # if x == 500:
            "break"
        
        
#Modul Perkalian
def perkalian(b):
    while True:
        angka = int(input("angkamu = "))
        ank = int(input("dikali dengan angka = "))
        print(f"{angka} * {ank} = {angka * ank}")
        
        # Hentikan program jika pengguna mengetik 'stop'    
        pilihan = input("Lanjut atau Stop? (lanjut/stop): ")   
                
        if pilihan == 'stop':
            print("Program selesai.")
            break
    
    
print("selesai")
