import os
os.system('cls')

# n, m, k = input().split()
# # n, m, k = int(input().split())
# n = int(n)
# m = int(m)
# k = int(k)
# print(n, m, k)
# print(type(n), type(m), type(k))

# a = int(input())
# if a == 1:
#     print("oke")
# else:
#     exit()

# y = lambda a : a + 10
# print(y(5))

# def y(a):
#     return a+10

# print(y(5))

# loc =[
#     [12,1],
#     [13,5],
#     [11,7],
#     [10,1]
# ]
# # urut = 
# print(sorted(loc, key=lambda x: (x[1], x[0])))

# y = lambda x: (x[1], x[0])
# print(y(loc))

# print(urut(listku))
# sorted()
# def purut(x):
#     return x[1], x[0]
# print(sorted(listku, key=purut))

l=[
    [12,1],
    [13,5],
    [11,7],
    [10,1]
]

# kolom
ba = sorted(l, key=lambda x: (x[1], x[0]))
print(ba)
# # baris
# ca = sorted(l, key=lambda x: (x[0], x[1]))
# print(ca)

# Format Output
a = 1
b = 2
print(a+1, b+1)
print("%d %d" % (a+1, b+1))
print('{} {}'.format (a+1, b+1))
print(f'{a+1} {b+1}')


# baris = [int(i) for i in input().split()]
# print(baris)