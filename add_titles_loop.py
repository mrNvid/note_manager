title_list = []
title_input = "1"
print('Введите заголовоки по очереди или оставте пустым для завершения:')
while title_input !="":
    title_input = input("Заголовок:")
    while title_input !="":
        if title_input in title_list:
            print("Заголовок уже существует")
        else:
            title_list.append(title_input)
            print("Добавлено")
        break
print("Все заголовки:", title_list)