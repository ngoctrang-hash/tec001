username = "X"
password = "L"
n = 0
while True:
    user = input('user: ')
    pw = input('pass: ')
    if pw != "L" or user != "X" and n < 5:
        print('fail')
        n += 1
    if n == 5:
        print('Access Denied')
        break
    if user == username and pw == password:
        print('Welcome')
        break