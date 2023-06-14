import random


number = random.randint(0,100)
#print(number)

user_number = None

count = 0


levels = {1:10,2:5,3:3}
level = int(input('Выберите уровень : ' ))
max_count = levels[level]

user_count = int(input('Введите количество пользователей : '))
users = []
for user in range(user_count):
    user_name = input(f'Введите имя пользователя: (user)')
    users.append(user_name)
    print(users)
while number != user_number:
    user_number = int(input('Введите число до 100 : '))
    count += 1

    if count == max_count:
        print('Вы проиграли!')
        break
    print('Попытка номер ' + str(count))
    if number < user_number:
        print('Ваше число больше загаданного.')
    elif number > user_number:
        print('Ваше число меньше загаданного.')
else:
    print('Победа!')
