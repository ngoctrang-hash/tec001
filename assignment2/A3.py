def ask():
    sex = input("Enter your biological sex:")
    hemoglobin = float(input("Enter your hemoglobin value:"))
    if sex == 'male' and 134 <= hemoglobin <= 167:
        print("normal")
    elif sex == 'male' and hemoglobin < 134:
        print("low")
    elif sex == 'male' and hemoglobin > 167:
        print("high")
    if sex == 'female' and 117 <= hemoglobin <= 155:
        print("normal")
    elif sex == 'female' and hemoglobin < 117:
        print("low")
    elif sex == 'female' and hemoglobin > 155:
        print("high")
ask()
