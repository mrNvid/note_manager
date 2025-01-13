

notes = [{'username': 'Андрей', 'title': 'Магазин', 'content': 'Помидоры купить', 'status': 'новый', 'issue_date': '18-01-2025', 'created_date': '13-01-2025'},
         {'username': 'Полина', 'title': 'Учёба', 'content': 'Сдать зачёт', 'status': 'В процессе', 'issue_date': '10-01-2025', 'created_date': '01-01-2025'},
         {'username': 'Эрик', 'title': 'Работа', 'content': 'Уволится', 'status': 'в процессе', 'issue_date': '01-02-2025', 'created_date': '01-01-2025'}]

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

display_notes(notes)