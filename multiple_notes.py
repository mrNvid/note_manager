from datetime import date

notes = []
variables = []
keys = ['username', 'title', 'content', 'status', 'issue_date', 'created_date']
print("Менеджер заметок")
print("Вы можете добавить новую заметку:")
while True:
    try:
        print('Новая заметка:')
        while True:
            variables.append(input('Введите имя:'))
            if variables[len(variables) - 1]:
                break
            else:
                del variables[len(variables) - 1]
                print("Вы ничего не ввели. Попробуйте снова")
        while True:
            variables.append(input('Введите заголовок заметки:'))
            if variables[len(variables) - 1]:
                break
            else:
                del variables[len(variables) - 1]
                print("Вы ничего не ввели. Попробуйте снова")
        while True:
            variables.append(input('Введите текст заметки:'))
            if variables[len(variables) - 1]:
                break
            else:
                del variables[len(variables) - 1]
                print("Вы ничего не ввели. Попробуйте снова")
        while True:
            variables.append(input('Введите статус заметки:'))
            if variables[len(variables) - 1]:
                break
            else:
                del variables[len(variables) - 1]
                print("Вы ничего не ввели. Попробуйте снова")
        while True:
            try:
                issue_date = input('Введите дату истечения заметки в формате дд-мм-гггг:').split('-')
                day, month, year = [int(item) for item in issue_date]
                issue_date.reverse()
                issue_date = date(year, month, day)
                variables.append(issue_date)
                if len(str(year)) == 4:
                    break
                else:
                    print('Неверный формат, попробуйте ещё раз')
            except Exception as e:
                print("Ошибка ввода, попробуйте ещё раз")
                print(e)
        while True:
            try:
                created_date = input('Введите дату истечения заметки в формате дд-мм-гггг:').split('-')
                day, month, year = [int(item) for item in created_date]
                created_date.reverse()
                created_date = date(year, month, day)
                variables.append(created_date)
                if len(str(year)) == 4:
                    break
                else:
                    print('Неверный формат, попробуйте ещё раз')
            except Exception as e:
                print("Ошибка ввода, попробуйте ещё раз")
                print(e)
        note = dict(zip(keys, variables))
        notes.append(note)
        new_note = input("Хотите добавить ещё одну заметку? (да/нет)")
        if new_note == "нет":
            break
    except Exception as e:
        print("Ошибка ввода, попробуйте ещё раз")
        print(e)

print('Все заметки:')
for i in range(len(notes)):
    print('_____________________')
    note = notes[i]
    for key, values in note.items():
        print(key,':', values)