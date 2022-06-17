number_of_tasks = int(input())
for n in range(number_of_tasks):
    number = int(input())
    for i in range(number - 1):
        if (i+2) == number:
            print('TAK')
            break
        if number % (i + 2) == 0:
            print('NIE')
            break


