from datetime import date
key = ['username', 'title', 'content', 'status', 'issue_date', 'created_date']
variables = []
def create_note():
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
            else: print('Неверный формат, попробуйте ещё раз')
        except Exception as e:
            print("Ошибка ввода, попробуйте ещё раз")
            print(e)
    variables.append(date.today())
    note = dict(zip(key, variables))
    return note
note = create_note()
print('Ваша заметка:')
print('_____________________')
for key, values in note.items():
    print(key,':', values)