height = int(input("Enter height: "))
width = int(input("Enter width: "))
countHeight = 0
if height < 0 and width < 0:
    print("Invalid input, program terminates.")
else:
    while countHeight <= height:
        countHeight += 1
        countWidth = width
        while countWidth >= width:
            if(countHeight % 2) == 0:
                print(" *", end='')
            if (countHeight % 2) != 0:
                print("* ", end='')
            countWidth -= 1
        print("")




