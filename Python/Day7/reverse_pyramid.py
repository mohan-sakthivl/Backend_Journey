row = 4
column = 7
space = 0

for i in range(row, 0, -1):

    for z in range(1, space + 1):
        print("   ", end=" ")

    for j in range(1, column + 1):
        print(" * ", end=" ")

    column -= 2
    space += 1

    print("\n",end="")
