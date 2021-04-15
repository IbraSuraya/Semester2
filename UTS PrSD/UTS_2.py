import os
from collections import deque as dq

os.system('cls')

Linked_list = dq([])
while True:
    x = input(":> ")
    if x == 'S' or x == 's': break
    Linked_list.appendleft(int(x))
    print(*Linked_list, sep=" -> ")
    # If kamu input S or s, maka program berhenti