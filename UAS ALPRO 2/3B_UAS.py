# Hapus terminal otomatis
import os
os.system('cls')

def main():
    # Input baris, kolom, dan kemenarikan
    n, m, k = [int(i) for i in input().split()]

    # batasan baris dan kolom
    if n < 1 and m < 1 and n > 100 and m > 100 : exit()

    # batasan kemenarikan
    if k < 1 and k > 10_000: exit()

    # var untuk petak nxm
    petak = []
    # var untuk koordinat yang nilai kemenarikannya = k
    loc = []

    # proses Input
    for _ in range(n):
        # inputan baris
        baris = [int(i) for i in input().split()]

        # batasan elemen harus = m
        if len(baris) == m:
            petak.append(baris)
            baris = []
        else: exit()

    # manggil fungsi proses
    proses(n, m, k, petak, loc)


def proses(n, m, k, petak, loc):

    # Penelusuran dari perbaris
    for i in range(n):
        for j in range(m):

            # var untuk nilai K
            hasil = 1

            # var untuk koordinat
            temp = []

            # atas
            if i > 0:
                hasil *= petak[i-1][j]
            # kiri
            if j > 0:
                hasil *= petak[i][j-1]
            # bawah
            if i < n-1:
                hasil *= petak[i+1][j]
            # kanan
            if j < m-1:
                hasil *= petak[i][j+1]

            # jika hasil = k, akan menyimpan nilai koordinatnya di temp
            if hasil == k:
                temp.append(i)
                temp.append(j)
                # menyimpan kordinat temp di kumpulan koordinat loc
                loc.append(temp)

    # jika sama sekali gk ada koordinat yang menghasilaka k
    if loc == []:
        # mencetak hasil koordinat kosong
        print('0 0')
    else:
        # proses pengurutaran berdasarkan kolom
        loc = sorted(loc, key=lambda x: (x[1], x[0]))
        # mencetak hasil koordinat yang paling kecil
        print(f'{loc[0][0]+1} {loc[0][1]+1}')

main()
"""
3 1
1 2
1 3
5 2
"""
