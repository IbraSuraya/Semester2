import os
def clear():
    os.system('cls')

class stack:
    def __init__(self):
        self.stack = []
    def delete(self):
        self.stack = []
        print("="*50)
        print("= ", self.stack)
        print("=    Stack is Empty")
        print("="*50)
    def push(self):
        print("="*50)
        x = int(input("= Silahkan Input: "))
        self.stack.append(x)
        print("= ", self.stack)
        print("="*50)
    def pop(self):
        if len(self.stack) == 0:
            print("="*50)
            print("=    Stack is Empty")
            print("="*50)
        else:
            print("="*50)
            print("= Keluar: ",self.stack[-1])
            self.stack.pop()
            print("= ", self.stack)
            print("="*50)
    def isEmpty(self):
        if len(self.stack) == 0:
            print("="*50)
            print("=    Stack is Empty")
            print("="*50)
        else:
            print("="*50)
            print("=    Stack is not Empty")
            print("="*50)
    def top(self):
        if len(self.stack) == 0:
            print("="*50)
            print("=    Stack is Empty")
            print("="*50)
        else:
            print("="*50)
            print("= Top: ",self.stack[-1])
            print("="*50)
    def display(self):
        print("="*50)
        print("= ", self.stack)
        print("="*50)
    def count(self):
        print("="*50)
        print("= Total: ", len(self.stack))
        print("= ", self.stack)
        print("="*50)
    def cek(self):
        if len(self.stack) == 0:
            print("="*50)
            print("=    Stack is Empty")
            print("="*50)
        else:
            print("="*50)
            x = int(input("= Silahkan data yang butuh dicek: "))
            if x in self.stack:
                print("= Berjumlah: ", self.stack.count(x))
            else:
                print("= Tidak ada didalam tumpukkan")
            print("="*50)
    def urutkan(self):
        print("="*50)
        self.stack.sort()
        print("Terurut: ", self.stack)
        print("="*50)

def konfirmasi():
    print("=    Silahkan Pilih [y = Kembali] [n = akhiri]   =\n", "="*50, sep="")
    temp = input("Pilihan anda = ")
    if temp == 'y' : Menu()
    else : pass

def pilihan(token):
    clear()
    if   token == '1': tumpuk.isEmpty(); konfirmasi()
    elif token == '2': tumpuk.display(); konfirmasi()
    elif token == '3': tumpuk.top(); konfirmasi()
    elif token == '4': tumpuk.push(); konfirmasi()
    elif token == '5': tumpuk.pop(); konfirmasi()
    elif token == '6': tumpuk.count(); konfirmasi()
    elif token == '7': tumpuk.cek(); konfirmasi()
    elif token == '8': tumpuk.delete(); konfirmasi()
    elif token == '9': tumpuk.urutkan(); konfirmasi()
    else:
        print("="*50,"\n=    Pilihan anda diluar batas yang ditentukan   =")
        konfirmasi()

def Menu():
    clear()
    print("="*50,"\n=\t\tPilih Operator Stack\t\t =\n", end='')
    print("="*50)
    print("= 1.IsEmpty\n"\
        "= 2.Isi Stack\n"\
        "= 3.Top\n"\
        "= 4.Push\n"\
        "= 5.Pop\n"\
        "= 6.Cek Total Stack\n"\
        "= 7.Cek Jumlah data tertentu\n"\
        "= 8.Hapus Semua Elemen\n"\
        "= 9.Urutakan Ascending")
    print("="*50)
    token = input("= Silahkan Input Pilihan anda: ")
    pilihan(token)

tumpuk = stack()
Menu()
