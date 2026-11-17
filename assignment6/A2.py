seasons = ("winter","winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter" )
month = int(input("Enter month 1-12:"))
if 1 <= month <= 12:
    print("The corresponding season", int(seasons-1))
else:
    print("Please enter month 1-12")