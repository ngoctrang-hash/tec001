
def task_6():
    string = input("string: ")
    length = len(string)
    if length == 0:
        return
    mid = length // 2
    result = ''
    for i in range(length):
        if length % 2 == 0:
            if i == mid - 1 or i == mid:
                result = result + string[i]
            else:
                if i == mid:
                    result = result + string[i]

    print(result)
task_6()
