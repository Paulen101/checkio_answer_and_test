print("multiplication table")
print("  |", end = " ")
for j in range(1, 10): 
    print("  ", j, end = " ")
print()
print("----------------------------------------------------")
for i in range(1, 10):
    if i % 2 == 0:
        print(i, "|", end = " ")
    for j in range(1, 10):
        if i % 2 == 0 and j % 2 == 0:
            print(format(i*j, "4d"), end = " ")
    print()



   