from datetime import datetime


def save_notes_to_file(notes, filename):
    key_ru = ['Имя пользователя', 'Заголовок', 'Описание', 'Статус', 'Дата создания', 'Дедлайн']
    with open(filename, 'a', encoding='utf-8') as file:
        for i in range(len(notes)):
            note = notes[i]
            note_content = ''
            b = 0
            for key, values in note.items():
                note_content += f"{key_ru[b]}: {values}\n"
                b += 1
            note_content += f"---\n"
            file.write(note_content)
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
    save_notes_to_file(notes, "filename.txt")