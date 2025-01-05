status = "нет"
print("Укажите новый статус заметки:")
print("1.Выполнено")
print("2.В процессе")
print("3.Отложено")
print("4.Ввести новый статус")
nomber_status=input()
while  int(nomber_status) <1 and int(nomber_status) >5:
    print("Ошибка ввода, попробуйте ещё раз")
if  nomber_status==1:
   status = "Выполнено"
elif int(nomber_status) == 2:
    status = "В процессе"
elif nomber_status == 3:
    status = "Отложено"
elif nomber_status == 4:
    status=input("Введите новый статус:")
print("Новый статус:",status)