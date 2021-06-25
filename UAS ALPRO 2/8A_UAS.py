# Hapus terminal Otomatis
import os
os.system('cls')

def proses(N, que_stack):

    for _ in range(N):
        # Input Peritah
        key = input()

        # untuk peritah Push
        if (key[0:4] == "push"):
            # untuk misah peritah dengan elemen
            key, data = key.split()
            data = int(data)
            # Batasan elemen
            if data < 0 and data > 1_000_000: exit()

            # Unutuk push back
            if key == "push_back": que_stack.append(data)
            # untuk push front
            elif key == "push_front": que_stack.insert(0, data)

        else:
            # pop back
            if key == "pop_back": que_stack.pop()
            # pop fornt
            elif key == "pop_front": que_stack.pop(0)

    print(*que_stack, sep="\n")

def main():
    # Deklarasi list
    que_stack = []
    # Input Batasan Perintah
    N = int(input())

    # Interval dari jumalh peritah
    if 1 <= N <= 10_000:
        proses(N, que_stack)
    else:
        exit()
        
main()