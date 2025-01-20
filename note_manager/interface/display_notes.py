

def display_page(notes, page):
    start_index = 0 + page * 5
    end_index = 5 + page * 5
    for index, note in enumerate(notes[start_index:end_index], start=1):
        print(f"""
        Номер заметки: {index}
        Имя пользователя: {note["username"]}
        Заголовок: {note["title"]}
        Описание: {note["content"]}
        Статус: {note["status"]}
        Дата Создания: {note["created_date"]}
        Дедлайн: {note["issue_date"]}
        """)
        print("_" * 50)

def display_notes(notes, page_number=0):
    if len(notes) == 0:
        print('Список заметок пуст')
    else:
        display_page(notes, page_number)
if __name__ == "__main__":
    notes = [{'username': 'Андрей', 'title': 'Магазин', 'content': 'Помидоры купить', 'status': 'новый',
              'issue_date': '18-01-2025', 'created_date': '13-01-2025'},
             {'username': 'Полина', 'title': 'Учёба', 'content': 'Сдать зачёт', 'status': 'В процессе',
              'issue_date': '10-01-2025', 'created_date': '01-01-2025'},
             {'username': 'Эрик', 'title': 'Работа', 'content': 'Уволится', 'status': 'в процессе',
              'issue_date': '01-02-2025', 'created_date': '01-01-2025'}, {'username': 'Андрей', 'title': 'Магазин', 'content': 'Помидоры купить', 'status': 'новый',
              'issue_date': '18-01-2025', 'created_date': '13-01-2025'},
             {'username': 'Полина', 'title': 'Учёба', 'content': 'Сдать зачёт', 'status': 'В процессе',
              'issue_date': '10-01-2025', 'created_date': '01-01-2025'},
             {'username': 'Эрик', 'title': 'Работа', 'content': 'Уволится', 'status': 'в процессе',
              'issue_date': '01-02-2025', 'created_date': '01-01-2025'}, {'username': 'Андрей', 'title': 'Магазин', 'content': 'Помидоры купить', 'status': 'новый',
              'issue_date': '18-01-2025', 'created_date': '13-01-2025'},
             {'username': 'Полина', 'title': 'Учёба', 'content': 'Сдать зачёт', 'status': 'В процессе',
              'issue_date': '10-01-2025', 'created_date': '01-01-2025'},
             {'username': 'Эрик', 'title': 'Работа', 'content': 'Уволится', 'status': 'в процессе',
              'issue_date': '01-02-2025', 'created_date': '01-01-2025'}]
    display_notes(notes)