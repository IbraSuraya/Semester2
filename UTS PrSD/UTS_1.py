"""
        UTS Prak.Struktur Data
Nama    : Ibra Hasan Suraya
NIM     : 2010511053
Kelas   : IF-B
Jurusan : Informatika 2020

Keterangan Pilihan
 1 = Periksan apakah antrian sudah penuh atau belum
 2 = Memasukkan inputan ke dalam antrian
 3 = Mengeluarkan antrian paling depan
 4 = Menampilkan antrian paling depan
 5 = Menampilkan antrian paling belakang
 6 = Menampilkan seluruh antrian
 7 = Menampilkan total antrian yang sudah ada
 8 = Menghentikan program

Urutan Kerja Program
- Meminta batasan kapasitas antrian
- Selanjutnya opsi pilihan operator
"""

import os               # Untuk mengganti tampilan layar, dengan menghapus layar sebelumnnya
def clear():
    os.system('cls')

class Queue:
    def __init__(self, nilai):         # Insialiasi Antrian
        self.queue = []
        self.size = nilai
    def enqueue(self):          # Proses penambahan antrian
        print("="*50)
        if len(self.queue) < self.size:
            x = int(input("= Silahkan Input: "))
            self.queue.append(x)
            print("= Ditambahkan: ", self.queue)
        else:
            print("= Kapasitas Antrian sudah Penuh")
            print("= ", self.queue)
        print("="*50)
    def dequeue(self):          # Proses pengambilan antrian paling depan
        print("="*50)
        if len(self.queue) == 0:
            print("=    Antrian anda sedang kosong")
        else:
            print("= Keluar: ",self.queue[0])
            self.queue.pop(0)
            print("= ", self.queue)
        print("="*50)
    def isEmpty(self):      # Pengecekan kondisi antrian
        print("="*50)
        if len(self.queue) == 0:
            print("=    Antrian sedang kosong")
        elif len(self.queue) < self.size:
            print("=    Slot masih tersedia: ", (self.size)-len(self.queue))
        else:
            print("=    Kapasitas Antrian sudah Penuh")
        print("="*50)
    def back(self):         # Menampilkan antrian paling belakang
        print("="*50)
        if len(self.queue) == 0:
            print("=    Antrian sedang kosong")
        else:
            print("= Antrian paling akhir: ",self.queue[-1])
        print("="*50)
    def front(self):        # Menampilkan antrian paling depan
        print("="*50)
        if len(self.queue) == 0:
            print("=    Antrian sedang kosong")
        else:
            print("= Antrian paling depan: ",self.queue[0])
        print("="*50)
    def display(self):      # Menampilkan keseluruhan antrian
        print("="*50)
        print("= ", self.queue)
        print("="*50)
    def count(self):        # Menghitung jumlah total antrian
        print("="*50)
        print("= Total antrian : ", len(self.queue))
        print("= Sisa Kapasitas: ", (self.size)-len(self.queue))
        print("= ", self.queue)
        print("="*50)

def ulangi():               # Fungsi pengulangan pilihan operator
    temp = input("Pilihan operator = ")
    pilihan (temp)

def pilihan(token):         # Proses penentuan pilihan operator
    clear()
    if   token == '1': antrian.isEmpty(); ulangi()
    elif token == '2': antrian.enqueue(); ulangi()
    elif token == '3': antrian.dequeue(); ulangi()
    elif token == '4': antrian.front(); ulangi()
    elif token == '5': antrian.back(); ulangi()
    elif token == '6': antrian.display(); ulangi()
    elif token == '7': antrian.count(); ulangi()
    elif token == '8': pass
    else:
        print("="*50,"\n= Pilihan anda diluar batas yang ditentukan (1-8)=")
        print("="*50)
        ulangi()

def Menu():             # Tampilan menu
    print("="*50,"\n=\t\tPilih Operator Queue\t\t =\n", end='')
    print("="*50)
    print("= 1.Periksa\n"\
        "= 2.Enqueue\n"\
        "= 3.Dequeu\n"\
        "= 4.Front Antrian\n"\
        "= 5.Back Antrian\n"\
        "= 6.Cek Isi antrian anda\n"\
        "= 7.Cek Total Queue\n"\
        "= 8. Hentikan Program")
    print("="*50)
    token = input("= Silahkan Input Pilihan anda: ")
    pilihan(token)


clear()
print("="*50,"\n=\t\tSelamat Datang\t\t\t =\n", end=''); print("="*50)
size_queue = int(input("Masukkan kapasitas antrian: "))
antrian = Queue(size_queue)
input("<ENTER>");clear()
Menu()
