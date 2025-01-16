from datetime import date
keys = ['username', 'title', 'content', 'status', 'issue_date', 'created_date']
variables = []
def create_note():
    print('Новая заметка:')
    while True:
        username = input('Введите имя:')
        if username != "":
            variables.append(username)
            break
        else:
            print("Вы ничего не ввели. Попробуйте снова")
    while True:
        title = input('Введите заголовок заметки:')

        if title != "":
            variables.append(title)
            break
        else:
            print("Вы ничего не ввели. Попробуйте снова")
    while True:
        content = input('Введите текст заметки:')
        if content != "":
            variables.append(content)
            break
        else:
            print("Вы ничего не ввели. Попробуйте снова")
    while True:
        status = input('Введите статус заметки:')
        if status != "":
            variables.append(status)
            break
        else:
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
    note = dict(zip(keys, variables))
    return note
note = create_note()
print('Ваша заметка:')
print('_____________________')
for key, values in note.items():
    print(key,':', values)