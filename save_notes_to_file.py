from fileinput import filename


def save_notes_to_file(notes, filename):
    key_ru = ['Имя пользователя', 'Заголовок', 'Описание', 'Статус', 'Дата создания', 'Дедлайн']
    file = open('filename', 'w', encoding='utf-8')
    for i in range(len(notes)):
        note = notes[i]
        b = 0
        for key, values in note.items():
            file.write(f"{key_ru[b]}: {values}\n")
            b += 1
        file.write(f"---\n")
    file.close()
if __name__ == "__main__":
    notes = [{'username': 'Андрей', 'title': 'Магазин', 'content': 'Помидоры купить', 'status': 'новый',
              'issue_date': '18-01-2025', 'created_date': '13-01-2025'},
             {'username': 'Полина', 'title': 'Учёба', 'content': 'Сдать зачёт', 'status': 'В процессе',
              'issue_date': '10-01-2025', 'created_date': '01-01-2025'},
             {'username': 'Эрик', 'title': 'Работа', 'content': 'Уволится', 'status': 'в процессе',
              'issue_date': '01-02-2025', 'created_date': '01-01-2025'}]
    save_notes_to_file(notes, filename)


