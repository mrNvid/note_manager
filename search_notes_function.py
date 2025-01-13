
notes = [{'username': 'Андрей', 'title': 'Магазин', 'content': 'Помидоры купить', 'status': 'новый', 'issue_date': '18-01-2025', 'created_date': '13-01-2025'},
         {'username': 'Полина', 'title': 'Учёба', 'content': 'Сдать зачёт', 'status': 'В процессе', 'issue_date': '10-01-2025', 'created_date': '01-01-2025'},
         {'username': 'Эрик', 'title': 'Работа', 'content': 'Уволится', 'status': 'в процессе', 'issue_date': '01-02-2025', 'created_date': '01-01-2025'}]

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
print('Вы можете ввести ключевое слово для поиска и/или нужный статус.')
print('Оставьте поле пустым, если критерий не требуется')
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
        print('Заметка №', i + 1)
        note = notes_view[i]
        for key, values in note.items():
            print(key, ':', values)
        print('_____________________')