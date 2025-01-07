from datetime import date

today = date.today()
print("Текущая дата:",today.strftime("%d.%m.%Y"))
while True:
    try:
        print("Введите дату дедлайна (в формате дд-мм-гггг):")
        issue_date = input().split('-')
        day, month, year = [int(item) for item in issue_date]
        issue_date.reverse()
        issue_date = date(year, month, day)
        break
    except:
        print("Ошибка ввода, попробуйте ещё раз")
delta_date = issue_date - today
if int(delta_date.days) >1:
    print(delta_date.days, "дней осталось до дедлайна")
elif delta_date.days == 0:
    print("Дедлайн сегодня!")
elif int(delta_date.days) < 1:
    print("Дедлайн просрочен на", abs(delta_date.days), "дней")