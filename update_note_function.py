from datetime import date

note = {'username': 'Андрей', 'title': 'Список дел', 'content': 'Купить хоз товары',
        'status': 'Новая', 'issue_date': '18-01-2025',
        'created_date': '11-01-2025'}

def chek_date(value):
        try:
            value = value.split('-')
            day, month, year = [int(item) for item in value]
            value = date(day, month,  year)
            if len(str(year)) == 4:
                return value
            else:
                eror = 'Неверный формат, попробуйте ещё раз'
                return eror
        except Exception as e:
            eror = "Ошибка ввода, попробуйте ещё раз"
            return eror

def update_note(note):
    print('Ваша заметка:')
    print('_____________________')
    for key, values in note.items():
        print(key, ':', values)
    print('Какие данные вы хотите обновить? (username, title, content, status, issue_date):')
    argument = input()
    while True:
        print('Введите новое значение:')
        value = input()
        if argument == 'issue_date':
            value = chek_date(value)
            if type(value) == str:
                eror = chek_date(value)
                print(eror)
            else:break
        else:
            break
    note[argument] = value
    print('Заметка обновлена:')
    print('_____________________')
    for key, values in note.items():
        print(key, ':', values)

update_note(note)