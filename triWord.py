size = int(input("Enter a number: "))

def print_ord(x):
    print(chr(ord('A') + col), end='')

row = 1
while row <= size:
    col = 0
    while col < row:
        print_ord(col)
        col = col + 1
    print()

    row = row + 1

while row - 2 > 0:
    col = 0
    while col < row - 2:
        print_ord(col)
        col = col + 1
    print()

    row = row - 1
