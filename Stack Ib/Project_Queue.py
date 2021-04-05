import os
def clear():
    os.system('cls')

class queue:
    def __init__(self):
        self.queue = []
    def delete(self):
        self.queue = []
        print("="*50)
        print("=    queue is Empty")
        print("="*50)
    def enqueue(self):
        print("="*50)
        x = int(input("= Silahkan Input: "))
        self.queue.append(x)
        print("= ", self.queue)
        print("="*50)
    def dequeue(self):
        if len(self.queue) == 0:
            print("="*50)
            print("=    queue is Empty")
            print("="*50)
        else:
            print("="*50)
            print("= Keluar: ",self.queue[0])
            self.queue.pop(0)
            print("= ", self.queue)
            print("="*50)
    def isEmpty(self):
        if len(self.queue) == 0:
            print("="*50)
            print("=    queue is Empty")
            print("="*50)
        else:
            print("="*50)
            print("=    queue is not Empty")
            print("="*50)
    def back(self):
        if len(self.queue) == 0:
            print("="*50)
            print("=    queue is Empty")
            print("="*50)
        else:
            print("="*50)
            print("= Back: ",self.queue[-1])
            print("="*50)
    def front(self):
        if len(self.queue) == 0:
            print("="*50)
            print("=    queue is Empty")
            print("="*50)
        else:
            print("="*50)
            print("= Front: ",self.queue[0])
            print("="*50)
    def display(self):
        print("="*50)
        print("= ", self.queue)
        print("="*50)
    def count(self):
        print("="*50)
        print("= Total: ", len(self.queue))
        print("= ", self.queue)
        print("="*50)
    def cek(self):
        if len(self.queue) == 0:
            print("="*50)
            print("=    queue is Empty")
            print("="*50)
        else:
            print("="*50)
            x = int(input("= Silahkan data yang butuh dicek: "))
            if x in self.queue:
                print("= Berjumlah: ", self.queue.count(x))
            else:
                print("= Tidak ada didalam antriankan")
            print("="*50)
    def urutkan(self):
        print("="*50)
        # new_list = []
        # while self.queue:
        #     minimum = self.queue[0] 
        #     for x in self.queue: 
        #         if x < minimum:
        #             minimum = x
        #             new_list.append(minimum)
        #             self.queue.remove(minimum)
        # print("= Terurut asc: ", new_list)

        self.queue.sort()
        print("Terurut: ", self.queue)
        print("="*50)

def konfirmasi():
    print("=    Silahkan Pilih [y = Kembali] [n = akhiri]   =\n", "="*50, sep="")
    temp = input("Pilihan anda = ")
    if temp == 'y' : Menu()
    else : pass

def pilihan(token):
    clear()
    if   token == '1': antrian.isEmpty(); konfirmasi()
    elif token == '2': antrian.display(); konfirmasi()
    elif token == '3': antrian.back(); konfirmasi()
    elif token == '4': antrian.front(); konfirmasi()
    elif token == '5': antrian.enqueue(); konfirmasi()
    elif token == '6': antrian.dequeue(); konfirmasi()
    elif token == '7': antrian.count(); konfirmasi()
    elif token == '8': antrian.cek(); konfirmasi()
    elif token == '9': antrian.delete(); konfirmasi()
    elif token == '10': antrian.urutkan(); konfirmasi()
    else:
        print("="*50,"\n=    Pilihan anda diluar batas yang ditentukan   =")
        konfirmasi()

def Menu():
    clear()
    print("="*50,"\n=\t\tPilih Operator Queue\t\t =\n", end='')
    print("="*50)
    print("= 1.IsEmpty\n"\
        "= 2.Isi Queue\n"\
        "= 3.Back\n"\
        "= 4.Front\n"\
        "= 5.Enqueue\n"\
        "= 6.Dequeue\n"\
        "= 7.Cek Total Queue\n"\
        "= 8.Cek Jumlah data tertentu\n"\
        "= 9.Hapus Semua Elemen\n"\
        "= 10.Urutakan Ascending")
    print("="*50)
    token = input("= Silahkan Input Pilihan anda: ")
    pilihan(token)

antrian = queue()
Menu()
