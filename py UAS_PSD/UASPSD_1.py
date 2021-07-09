''' ===  NO.1  ===
UAS Praktikum Struktur Data 2021
Nama    : Ibra Hasan Suraya
Kelas   : IF-B
NIM     : 2010511053
Jurusan : Informatika
Dosen   : Pak Jayanta
Sumber	: Ebook Data Structures and Algorithms with Python (Kent D Lee)
Referen	  https://www.geeksforgeeks.org/find-paths-given-source-destination/
'''

# Tambahan, agar hapus terminal secara otomatis
import os
os.system('cls')

# Memanggil tipe data dict yang valuenya berupa tipe data apapun
from collections import defaultdict

# Membuat Objek Graf
class Graph:

	# Deklarasi graf
	def __init__(self, vertices):
		# Objek yang menampung vertex
		self.V = vertices
		# Dekalarasi Graf dengan tipe data dict bervalue list
		self.graph = defaultdict(list)
		# Deklarasi untuk menampung bobot tiap jalur
		self.bobot = {}

	# Proses pembuatan jalur
	def tambahEdge(self, dari, ke, w):

		self.graph[dari].append(ke)
		self.bobot[(dari,ke)] = w
	
	def cariJalur(self, u, akhir, visited, path):

		# Vertex awal diubah ke True
		visited[u]= True
		# Karena sudah true, di append ke dalam path
		path.append(u)

		# Jika sudah pada u vertex tujuan, maka mencetak jalur tersebut
		if u == akhir:
			print(path)
		else:
			# Menelusuri vertex yang terhubung pada u saat tertentu
			for i in self.graph[u]:
				# Jika vertex ini masih false
				if visited[i]== False:
					# Maka akan menjadi u yang baru saat pemanggialn fungsi CariJalur
					self.cariJalur(i, akhir, visited, path)
		
		# Menghapus vertex yang sudah dilewati dan vertex yang lebih dari 17
		path.pop()
		# Jika sudah di append di path, maka status u akan di false kembali
		# Karena ada kemungkinan akan dilewati
		visited[u]= False

	# Fungsi Persiapan mencari jalur
	def jalur(self, awal, akhir):

		# Memberi tanda bahwa semua vertex yang dilalui masih false
		visited =[False]*(self.V)
		# Var penampung jalur yang ingin diketahui
		path = []
		# Memanggil fungsi proses pencarian
		self.cariJalur(awal, akhir, visited, path)

g = Graph(30)
g.tambahEdge(0, 1, 2.02)
g.tambahEdge(1, 4, 1.70)
g.tambahEdge(2, 8, 4.64)
g.tambahEdge(3, 0, 4.45)
g.tambahEdge(3, 2, 5.53)
g.tambahEdge(4, 5, 3.28)
g.tambahEdge(5, 7, 4.28)
g.tambahEdge(5, 12, 3.30)
g.tambahEdge(6, 2, 3.41)
g.tambahEdge(7, 22, 16.43)
g.tambahEdge(8, 13, 8.45)
g.tambahEdge(9, 3, 5.02)
g.tambahEdge(9, 10, 2.32)
g.tambahEdge(9, 17, 7.10)
g.tambahEdge(10, 0, 6.20)
g.tambahEdge(10, 1, 5.80)
g.tambahEdge(10, 11, 1.67)
g.tambahEdge(10, 17, 8.65)
# g.tambahEdge(11, )
g.tambahEdge(12, 11, 2.16)
g.tambahEdge(13, 14, 4.61)
g.tambahEdge(13, 16, 7.32)
g.tambahEdge(14, 15, 4.07)
g.tambahEdge(14, 17, 13.47)
g.tambahEdge(15, 16, 1.24)
g.tambahEdge(15, 17, 8.81)
g.tambahEdge(16, 17, 9.01)
g.tambahEdge(17, 3, 10.81)
g.tambahEdge(17, 6, 11.6)
g.tambahEdge(17, 23, 11.76)
g.tambahEdge(17, 24, 8.42)
g.tambahEdge(18, 17, 4.07)
g.tambahEdge(19, 18, 1.54)
g.tambahEdge(20, 19, 1.53)
g.tambahEdge(21, 20, 6.17)
g.tambahEdge(21, 22, 4.66)
# g.tambahEdge(22, )
g.tambahEdge(23, 24, 2.18)
g.tambahEdge(24, 27, 4.67)
g.tambahEdge(25, 18, 6.17)
g.tambahEdge(25, 26, 1.86)
g.tambahEdge(26, 19, 4.72)
g.tambahEdge(27, 25, 3.51)
g.tambahEdge(27, 29, 11.6)
g.tambahEdge(28, 20, 9.32)
g.tambahEdge(28, 21, 6.66)
g.tambahEdge(28, 29, 4.24)
# g.tambahEdge(29, )

awal = 9 ; akhir = 29
print("Berikut semua kemungkin jalur")
print(f"Dari: {awal} Menuju: {akhir}")
g.jalur(awal, akhir)