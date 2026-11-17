number = []
while True:
    user = input("Enter number (enter to break):")
    if user == "":
        break
    number.append(int(user))
number.sort(reverse=True)
number = number[:5]
print(number)



