from datetime import date

notes = [{'username': 'Андрей', 'title': 'Магазин', 'content': 'Помидоры купить', 'status': 'новый', 'issue_date': datetime.date(2025, 1, 18), 'created_date': datetime.date(2025, 1, 13)},
         {'username': 'Полина', 'title': 'Учёба', 'content': 'Сдать зачёт', 'status': 'В процессе', 'issue_date': datetime.date(2025, 1, 20), 'created_date': datetime.date(2025, 1, 1)},
         {'username': 'Эрик', 'title': 'Работа', 'content': 'Уволится', 'status': 'в процессе', 'issue_date': datetime.date(2025, 6, 2), 'created_date': datetime.date(2025, 1, 1)}]

def display_notes(notes):
