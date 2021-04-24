'''
Nama	: Ibra Hasan Suraya
Kelas	: IF-B
Jurusan	: Informatika
Referens: Modifikasi sendiri + https://www.geeksforgeeks.org hapus-binary-tree/

Catatan:
Dikarenakan jumlah input banyak, terdapat singkatan
r = right
l = left
Untuk mempersingkat kata per line
'''

import os
os.system('cls')

'''Pembuatan B-Tree'''
class Node:
    urutan_input=[]

    def __init__(self,data):
        self.urutan_input.append(data)
        self.data = data
        self.l = None
        self.r = None
    
    def info(self):
        print(*self.urutan_input)

'''Sort Inorder '''
def inorder(temp):      # Inorder (L-N-R)
	if(not temp):
		return
	inorder(temp.l)
	print(temp.data, end = " ")
	inorder(temp.r)

'''Sort Preorder '''
def pretorder(temp):    # Preorder (N-L-R)
	if(not temp):
		return
	print(temp.data, end = " ")
	pretorder(temp.l)
	pretorder(temp.r)

'''Sort Postorder '''
def postorder(temp):    # Postorder (L-R-N)
	if(not temp):
		return
	postorder(temp.l)
	postorder(temp.r)
	print(temp.data, end = " ")

'''Proses Penghapusan paling akhir'''
def hapus_terbawah(root,d_node):
	list_node = []
	list_node.append(root)
	while(len(list_node)):
		temp = list_node.pop(0)
		if temp is d_node:
			temp = None
			return
		if temp.r:
			if temp.r is d_node:
				temp.r = None
				return
			else:
				list_node.append(temp.r)
		if temp.l:
			if temp.l is d_node:
				temp.l = None
				return
			else:
				list_node.append(temp.l)

'''Proses Penghapusan node tertentu'''
def hapus(root, key):
	if root == None :
		return None
	if root.l == None and root.r == None:
		if root.key == key :
			return None
		else :
			return root
	key_node = None
	list_node = []
	list_node.append(root)
	while(len(list_node)):
		temp = list_node.pop(0)
		if temp.data == key:
			key_node = temp
		if temp.l:
			list_node.append(temp.l)
		if temp.r:
			list_node.append(temp.r)
	if key_node :
		x = temp.data
		hapus_terbawah(root,temp)
		key_node.data = x
	return root

'''Proses Inputan'''
root = Node(15)
root.l = Node(25)
root.r = Node(20)
root.l.l = Node(30)
root.l.r = Node(10)
root.r.l = Node(7)
root.r.r = Node(13)
root.l.l.l = Node(14)
root.l.l.r = Node(6)
root.l.r.l = Node(9)
root.l.r.r = Node(11)
root.r.l.l = Node(17)
root.r.l.r = Node(27)
root.r.r.l = Node(32)
root.r.r.r = Node(23)


'''Proses Outputan'''
print("Urutan Input:\t", end=""); root.info()
print("\nSebelum di hapus:")
print("In:\t", end=""); inorder(root); print()       # Inorder (L-N-R)
print("Pre:\t", end=""); pretorder(root); print()    # Preorder (N-L-R)
print("Post:\t", end=""); postorder(root); print()   # Postorder (L-R-N)

print("\nSetelah di hapus;")
key = 25
root = hapus(root, key)
print("Node yang dihapus: ", key)
print("In:\t", end=""); inorder(root); print()       # Inorder (L-N-R)
print("Pre:\t", end=""); pretorder(root); print()    # Preorder (N-L-R)
print("Post:\t", end=""); postorder(root); print()   # Postorder (L-R-N)

