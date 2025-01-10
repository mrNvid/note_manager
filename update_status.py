status = "В процессе"
print('Текущий статус:', status)
print("Укажите новый статус заметки:")
print("1.Выполнено")
print("2.В процессе")
print("3.Отложено")
print("4.Ввести новый статус")
while True:
    nomber_status=input()
    if  int(nomber_status)==1:
        status = "Выполнено"
        break
    elif int(nomber_status) == 2:
        status = "В процессе"
        break
    elif int(nomber_status) == 3:
        status = "Отложено"
        break
    elif int(nomber_status) == 4:
        status=input("Введите новый статус:")
        break
    else: print("Ошибка ввода, попробуйте ещё раз")
print("Новый статус:",status)