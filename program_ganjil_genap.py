# Meminta input angka dari pengguna
angka = int(input("Masukkan sebuah angka: "))

# Mengecek sisa bagi dengan 2
if angka % 2 == 0:
    print(f"Angka {angka} adalah bilangan genap.")
else:
    print(f"Angka {angka} adalah bilangan ganjil.")
