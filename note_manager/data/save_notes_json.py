import json
from datetime import datetime

def save_notes_json(notes, filename):
    with open('filrname.json', 'w', encoding='utf-8') as file:
        file = json.dump(notes, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":

    current_date = str(datetime.now())
    notes = [
        {
            'username': 'Андрей',
            'title': 'Магазин',
            'content': 'Помидоры купить',
            'status': 'новый',
            'issue_date': '18-01-2025',
            'created_date': current_date
        },
        {
            'username': 'Полина',
            'title': 'Учёба',
            'content': 'Сдать зачёт',
            'status': 'В процессе',
            'issue_date': '10-01-2025',
            'created_date': current_date
        },
        {
            'username': 'Эрик',
            'title': 'Работа',
            'content': 'Уволится',
            'status': 'в процессе',
            'issue_date': '01-02-2025',
            'created_date': current_date
        }
    ]
    save_notes_json(notes, 'filename.json')