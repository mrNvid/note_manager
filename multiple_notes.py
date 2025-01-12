from datetime import date

notes = []
print("Менеджер заметок")
print("Вы можете добавить новую заметку:")
while True:
    note = {'username': '', 'title': '', 'content': '', 'status': '', 'issue_date': '', 'created_date': ''}
    try:
        print('Новая заметка:')
        notes.append(note)
        while True:
            username = (input('Введите имя:'))
            note.update({'username': username})
            if username:
                break
            else:
                print("Вы ничего не ввели. Попробуйте снова")
        while True:
            title = (input('Введите заголовок:'))
            note.update({'title': title})
            if title:
                break
            else:
                print("Вы ничего не ввели. Попробуйте снова")
        while True:
            content = (input('Введите описание:'))
            note.update({'content': content})
            if content:
                break
            else:
                print("Вы ничего не ввели. Попробуйте снова")
        while True:
            status = (input('Введите статус:'))
            note.update({'status': status})
            if status:
                break
            else:
                print("Вы ничего не ввели. Попробуйте снова")
        while True:
            try:
                issue_date = input('Введите дату истечения заметки в формате дд-мм-гггг:').split('-')
                day, month, year = [int(item) for item in issue_date]
                issue_date.reverse()
                issue_date = date(year, month, day)
                note.update({'issue_date': issue_date})
                if len(str(year)) == 4:
                    break
                else:
                    print('Неверный формат, попробуйте ещё раз')
            except Exception as e:
                print("Ошибка ввода, попробуйте ещё раз")
                print(e)
        while True:
            try:
                created_date = input('Введите дату создания заметки в формате дд-мм-гггг:').split('-')
                day, month, year = [int(item) for item in created_date]
                created_date.reverse()
                created_date = date(year, month, day)
                note.update({'created_date': created_date})
                if len(str(year)) == 4:
                    break
                else:
                    print('Неверный формат, попробуйте ещё раз')
            except Exception as e:
                print("Ошибка ввода, попробуйте ещё раз")
                print(e)
        new_note = input("Хотите добавить ещё одну заметку? (да/нет)")
        if new_note == "нет":
            break
    except Exception as e:
        print("Ошибка ввода, попробуйте ещё раз")
        print(e)
print(notes)
print('Все заметки:')
for i in range(len(notes)):
    print('_____________________')
    note = notes[i]
    for key, values in note.items():
        print(key,':', values)