'''
Nama	: Ibra Hasan Suraya
Kelas	: IF-B
Jurusan	: Informatika 2020
Referens: Modifikasi sendiri + https://www.geeksforgeeks.org/deletion-binary-tree/

'''

import os
os.system('cls')

'''Pembuatan B-Tree'''
class Node:
	urutan_input=[]
	
	'''Proses Input'''
	def __init__(self,data):
		self.urutan_input.append(data)
		self.data = data
		self.left = None
		self.right = None
    
	'''Cetak'''
	def info(self):
		print(*self.urutan_input)

'''Proses Traversal'''
'''Sort Inorder '''
def inorder(temp):      # Inorder (L-N-R)
	if(not temp):
		return
	inorder(temp.left)
	print(temp.data, end = " ")
	inorder(temp.right)

'''Sort Preorder '''
def preorder(temp):    # Preorder (N-L-R)
	if(not temp):
		return
	print(temp.data, end = " ")
	preorder(temp.left)
	preorder(temp.right)

'''Sort Postorder '''
def postorder(temp):    # Postorder (L-R-N)
	if(not temp):
		return
	postorder(temp.left)
	postorder(temp.right)
	print(temp.data, end = " ")

'''Proses Inputan'''
root = Node(15)
root.right = Node(25)
root.right.left = Node(20)
root.right.right = Node(30)
root.right.left.left = Node(17)
root.right.left.right = Node(23)
root.right.right.left = Node(27)
root.right.right.right = Node(32)
root.left = Node(10)
root.left.left = Node(7)
root.left.right = Node(13)
root.left.left.left = Node(6)
root.left.left.right = Node(9)
root.left.right.left = Node(11)
root.left.right.right = Node(14)

'''Hasil Traversal'''
print("Urutan Input:\t", end=""); root.info()
print("\nHasil Traversal dan Sebelum di hapus:")
print("In:\t", end=""); inorder(root); print()       # Inorder (L-N-R)
print("Pre:\t", end=""); preorder(root); print()    # Preorder (N-L-R)
print("Post:\t", end=""); postorder(root); print()   # Postorder (L-R-N)