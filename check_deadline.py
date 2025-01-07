from datetime import date

today = date.today()
print("Текущая дата:",today.strftime("%d.%m.%Y"))
print("Введите дату дедлайна (в формате день-месяц-год):")
issue_date = input().split('-')
print(issue_date)
day, month, year = [int(item) for item in issue_date]
issue_date.reverse()
issue_date = date(year, month, day)
delta_date = issue_date - today
if int(delta_date.days) >1:
    print(delta_date.days, "дней осталось до дедлайна")
elif delta_date.days == 0:
    print("Дедлайн сегодня!")
elif int(delta_date.days) < 1:
    print("Дедлайн просрочен на", abs(delta_date.days), "дней")