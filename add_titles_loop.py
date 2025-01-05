title_list = []
title_input = "1"
print('Введите заголовоки по очереди или оставте пустым для завершения:')
while title_input !="":
    title_input = input("Заголовок:")
    while title_input !="":
        title_list.append(title_input)
        break
print(title_list)