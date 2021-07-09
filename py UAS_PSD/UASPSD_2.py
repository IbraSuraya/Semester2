''' ===  NO.2  ===
UAS Praktikum Struktur Data 2021
Nama    : Ibra Hasan Suraya
Kelas   : IF-B
NIM     : 2010511053
Jurusan : Informatika
Dosen   : Pak Jayanta
'''
# Ini Cuma Opsi Tambahan
import os
os.system('cls')    # Untuk Hapus Terminal secara otomatis

# Input Jumlah langkah deret fibo (n)
n = int(input("Masukkan Jumlah Langkah: "))

# Batasan agar n tidak bernilai negatif
if n <= 0:
    input("Inputan anda bernilai negatif\n[ENTER]")
    # jika sudah klik enter, program akan berhenti
    exit()  # Fungsi untuk menghentikan program

# Variabel Penampung Deret Fibo
lisFibo = []

# Fungsi Fibonacci dengan Metode Recursive
# Fungsi ini akan mengembalikan elemen fibonacci paling akhir (n+1)
def hasilFibo(n):
    # Alasan n=0 or n=1, sebagai batas bahwa deret fibonanci dimulai dari 0 lalu 1
    # Jika n=0, mengidentifikasikan bahwa dalam deret hanya 1 elemen yaitu 0 saja, maka return n itu sendiri
    # JIka n=1, mengidentifikasikan bahwa deret sebelumnya hanya 0, dan jika dijumlahkan dengan dirinya menghasilkan dirinya sendiri
    if (n==0) or (n==1):
        return n
    # Alasan direkursif dengan pengurangan, karena kita akan memulai dengan n=0 dan n=1
    # Alasan -1 dan -2, karena kita akan menjumlah elemen yang bersebelahan
    else:
        return (hasilFibo(n-1) + hasilFibo(n-2))

# Fungsi untuk menampilakan deret sebanyak n langkah / (n+1) elemen deret
# Alasan (n+1) elemen, karena ditambah elemen 0, pada awal deret
def deretFibo(n):
    # Cek batasan, apakah n bernilai negatif/positif?
    if n <= 0:
        return "Masukkan Angka Bulat Positif"
    else:
        # Alasan hingga n+1, agar elemen terakhir pada fungsi hasilFibo ikut dalam deretan
        for i in range(n+1):
            # Ditambahkan secara berurutan sebanyak 9 langkah yang masing2 di proses ke dalam fungsi hasilFibo
            lisFibo.append(hasilFibo(i))

# Mencetak elemen deret akhir
print(f"Elemen setelah langkah ke-{n}: {hasilFibo(n)}")
# Membuat deret Fibonanci dalam bentuk urutan
deretFibo(n)
# Mencetak deret Fibonanci
print("\nDeret Fibonacci:")
print(*lisFibo, sep=", ")
