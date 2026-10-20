def task_7():
    phrase = input('phrase: ')
    words = phrase.split()
    acronym = ''
    for word in words:
        acronym = acronym + word[0].upper()
    print(acronym)
task_7()