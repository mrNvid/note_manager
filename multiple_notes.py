from datetime import date

notes = []
names=[]
title = []
content = []
status = []
created_dates = []
issue_dates = []
values = []
print("Менеджер заметок")
print("Вы можете добавить новую заметку:")
while True:
    try:
        print('Новая заметка:')
        names.append(input('Введите имя:'))
        title.append(input('Введите заголовок заметки:'))
        content.append(input('Введите текст заметки:'))
        status.append(input('Введите статус заметки:'))
        created_date = input('Введите дату создания заметки в формате дд-мм-гггг:').split('-')
        day, month, year = [int(item) for item in created_date]
        created_date.reverse()
        created_date = date(year, month, day)
        created_dates.append(created_date)
        issue_date = input('Введите дату истечения заметки в формате дд-мм-гггг:').split('-')
        day, month, year = [int(item) for item in issue_date]
        issue_date.reverse()
        issue_date = date(year, month, day)
        issue_dates.append(issue_date)
        notes = [{'Имя': names[i], 'Заголовок': title[i], 'Заметка': content[i],
                  'Статус': status[i], 'Дата создания': created_dates[i],
                  'Дедлайн': issue_dates[i]}
                 for i in range(len(names))]
        new_note = input("Хотите добавить ещё одну заметку? (да/нет)")
        if new_note == "нет":
            break
    except Exception as e:
        print("Ошибка ввода, попробуйте ещё раз")
        print(e)

print('Все заметки:')
for i in range(len('Имя')):
    print('_____________________')
    note = notes[i]
    for key, values in note.items():
        print(key,':', values)