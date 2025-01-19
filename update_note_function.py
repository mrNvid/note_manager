from datetime import date

note = {'username': 'Андрей', 'title': 'Список дел', 'content': 'Купить хоз товары',
        'status': 'Новая', 'issue_date': '18-01-2025',
        'created_date': '11-01-2025'}

def chek_date(value):
    try:
        value = value.split('-')
        day, month, year = [int(item) for item in value]
        value.reverse()
        value = date(year, month, day)
        if len(str(year)) == 4:
            return value
        else:
            raise ValueError('Год должен быть в формате гггг')
    except Exception as e:
        print(e)
        return e

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
            if type(value) == date:
                value = value.strftime('%d-%m-%Y')
                break
        else:
            break

    note[argument] = value
    print('Заметка обновлена:')
    print('_____________________')
    for key, values in note.items():
        print(key, ':', values)
if __name__ == "__main__":
    update_note(note)