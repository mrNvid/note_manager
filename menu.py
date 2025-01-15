from datetime import date

notes = [{'username': 'Андрей', 'title': 'Магазин', 'content': 'Помидоры купить', 'status': 'новый', 'issue_date': '18-01-2025', 'created_date': '13-01-2025'},
         {'username': 'Полина', 'title': 'Учёба', 'content': 'Сдать зачёт', 'status': 'В процессе', 'issue_date': '10-01-2025', 'created_date': '01-01-2025'},
         {'username': 'Эрик', 'title': 'Работа', 'content': 'Уволится', 'status': 'в процессе', 'issue_date': '01-02-2025', 'created_date': '01-01-2025'}]

def chek_date(value):
    try:
        value = value.split('-')
        day, month, year = [int(item) for item in value]
        value.reverse()
        value = date(year, month, day)
        if len(str(year)) == 4:
            return value
        else:
            eror = 'Неверный формат, попробуйте ещё раз'
            return eror
    except Exception as e:
        eror = "Ошибка ввода, попробуйте ещё раз"
        return eror

def create_note():
    keys = ['username', 'title', 'content', 'status', 'issue_date', 'created_date']
    variables = []
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
    note = dict(zip(keys, variables))
    notes.append(note)

def display_notes(notes):
    if len(notes) == 0:
        print('Список заметок пуст')
    else:
        print('Все заметки:')
        for i in range(len(notes)):
            print('Заметка №',i+1)
            note = notes[i]
            for key, values in note.items():
                print(key, ':', values)
            print('_____________________')

def update_note(note):
    print('Ваша заметка:')
    print('_____________________')
    for key, values in note.items():
        print(key, ':', values)
    while True:
        print('Какие данные вы хотите обновить? (username, title, content, status, issue_date):')
        argument = input()
        if argument in note and argument !='created_date':
            break
        else:
            print('Ошибка, попробуйте снова')
    while True:
        print('Введите новое значение:')
        value = input()
        if argument == 'issue_date':
            value = chek_date(value)
            if type(value) == str:
                eror = chek_date(value)
                print(eror)
            else:
                value = value.strftime('%d-%m-%Y')
                break
        else:
            break

    note[argument] = value
    print('Заметка обновлена:')
    print('_____________________')
    for key, values in note.items():
        print(key, ':', values)

def delete_note():
    while True:
        try:
            coincidences = 0
            print('Все заметки:')
            for i in range(len(notes)):
                print('_____________________')
                note = notes[i]
                for key, values in note.items():
                    print(key, ':', values)
            condition_del = input('Введите имя пользователя или заголовок для удаления заметки:')
            if len(notes) == 0:
                print('Список заметок пуст!')
            else:
                for i in range(len('username')):
                    note = notes[i]
                    if condition_del.lower() == note['username'].lower() or condition_del.lower() == note['title'].lower():
                        del notes[i]
                        coincidences = 1
                        break
                if coincidences == 1:
                    print('-----------------------')
                    print('Успешно удалено. Остались следующие заметки:')
                    break
                else:
                    print('Заметок с таким именем пользователя или заголовком не найдено.')
        except Exception as e:
            print("Ошибка ввода, попробуйте ещё раз")
            print(e)

def search_notes(notes, keyword=None, status=None):
    notes_view = []
    if keyword and not status:
        for i in range(len(notes)):
            note = notes[i]
            for key, values in note.items():
                if values.lower() == keyword.lower():
                    notes_view.append(note)

    if status and not keyword:
        for i in range(len(notes)):
            note = notes[i]
            if note['status'].lower() == status.lower():
                notes_view.append(note)

    if status and keyword:
        for i in range(len(notes)):
            note = notes[i]
            if note['status'].lower() == status.lower():
                for key, values in note.items():
                    if values.lower() == keyword.lower():
                        notes_view.append(note)

    return notes_view

print('Добро пожаловать в менеджер заметок!')
while True:
    print('Выберете одно из доступных действий меню.')
    print('________________________________________')
    print('Меню действий:')
    print('1. Создать новую заметку')
    print('2. Показать все заметки')
    print('3. Обновить заметку')
    print('4. Удалить заметку')
    print('5. Найти заметки')
    print('6. Выйти из программы')
    print('________________________________________')
    user_input = input('Введите номер действия:')
    print('Ваш выбор:', user_input)
    print('________________________________________')
    if user_input == '1':
        create_note()
    elif user_input == '2':
        display_notes(notes)
    elif user_input =='3':
        update_note(note)
    elif user_input =='4':
        delete_note()
    elif user_input =='5':
        print('Вы можете ввести ключевое слово для поиска и/или нужный статус.')
        print('Оставьте поле пустым, если критерий не требуется')
        print('_____________________')
        keyword = input('Введите ключевое слово:')
        status = input('Введите нужный статус:')
        notes_view = search_notes(notes, keyword, status)
        if len(notes_view) == 0:
            if len(notes) == 0:
                print('Список заметок пуст')
            else:
                print('Совпадений не найдено')
        else:
            for i in range(len(notes_view)):
                print('_____________________')
                print('Заметка №', i + 1)
                print('_____________________')
                note = notes_view[i]
                for key, values in note.items():
                    print(key, ':', values)
                print('_____________________')
    elif user_input =='6':
        print('_____________________')
        print('Программа завершена. Спасибо за использование!')
        print('_____________________')
        break
    else: print('Ошибка ввода, попробуйте снова')