import os
os.system('cls')

Linked_list = []
while True:
    x = input(":> ")
    if x == 'S' or x == 's': break
    Linked_list.append(int(x))
    print(Linked_list)
    # If kamu input S or s, maka program berhenti