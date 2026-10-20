while True:
    inches = float(input("Enter inches:"))
    if inches < 0:
        break
    cm = inches * 2.54
    print(cm)
