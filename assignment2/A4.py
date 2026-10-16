def year():
    y = int(input("Enter a year:"))
    if y % 4==0:
        print("leap year")
    elif y %100==0 and y %400==0:
        print("leap year")
    else:
        print("not")
year()
