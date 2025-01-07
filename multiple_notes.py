from datetime import date

notes = []
note = {}
print("Менеджер заметок")
print("Вы можете добавить новую заметку:")
while True:
    try:
        print('Новая заметка:')
        name = input('Введите имя:')
        title = input('Введите заголовок заметки:')
        content = input('Введите текст заметки:')
        status = input('Введите статус заметки:')
        created_date = input('Введите дату создания заметки в формате дд-мм-гггг:').split('-')
        day, month, year = [int(item) for item in created_date]
        created_date.reverse()
        created_date = date(year, month, day)
        issue_date = input('Введите дату истечения заметки в формате дд-мм-гггг:').split('-')
        day, month, year = [int(item) for item in issue_date]
        issue_date.reverse()
        issue_date = date(year, month, day)
        note.update({'Имя': name, 'Заголовок' : title, 'Описание' : content, 'Статус': status, 'Дата создания': created_date,'Дедлайн': issue_date},)
        notes.append(note)
        note.clear()
        new_note = input("Хотите добавить ещё одну заметку? (да/нет)")
        if new_note == "нет":
            break
    except Exception as e:
        print("Ошибка ввода, попробуйте ещё раз")
        print(e)

print('Все заметки:')
a=0
while True:
    try:
        for key, values in notes[a].items():
            print(key,':', values)
            a=a+1
    except Exception as e:
        print(e)