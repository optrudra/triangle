rows = 8

for i in range(0, rows + 1):
    for j in range(1, i):
        print(j, end=" ")
        print()
             
for i in range(rows + 1, 0, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()
        