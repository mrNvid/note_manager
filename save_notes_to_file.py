from fileinput import filename
import yaml


def save_notes_to_file(notes, filename):
    key_ru = ['Имя пользователя', 'Заголовок', 'Описание', 'Статус', 'Дедлайн', 'Дата создания']
    with open('filename.yaml', 'w', encoding='utf-8') as file:
        for i in range(len(notes)):
            note = notes[i]
            note = dict(zip(key_ru, list(note.values())))
            yaml.dump([note], file, allow_unicode=True, sort_keys=False)
    file.close()
if __name__ == "__main__":
    notes = [{'username': 'Андрей', 'title': 'Магазин', 'content': 'Помидоры купить', 'status': 'новый',
              'issue_date': '18-01-2025', 'created_date': '13-01-2025'},
             {'username': 'Полина', 'title': 'Учёба', 'content': 'Сдать зачёт', 'status': 'В процессе',
              'issue_date': '10-01-2025', 'created_date': '01-01-2025'},
             {'username': 'Эрик', 'title': 'Работа', 'content': 'Уволится', 'status': 'в процессе',
              'issue_date': '01-02-2025', 'created_date': '01-01-2025'}]

    save_notes_to_file(notes, filename)


