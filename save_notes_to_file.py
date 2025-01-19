from fileinput import filename

notes = [{'username': 'Андрей', 'title': 'Магазин', 'content': 'Помидоры купить', 'status': 'новый', 'issue_date': '18-01-2025', 'created_date': '13-01-2025'},
         {'username': 'Полина', 'title': 'Учёба', 'content': 'Сдать зачёт', 'status': 'В процессе', 'issue_date': '10-01-2025', 'created_date': '01-01-2025'},
         {'username': 'Эрик', 'title': 'Работа', 'content': 'Уволится', 'status': 'в процессе', 'issue_date': '01-02-2025', 'created_date': '01-01-2025'}]
key_ru = ['Имя пользователя', 'Заголовок', 'Описание', 'Статус', 'Дата создания', 'Дедлайн']
def save_notes_to_file(notes, filename):
    file = open('filename.txt', 'w', encoding='utf-8')
    for i in range(len(notes)):
        file.write(f"Заметка №'{i + 1}\n")
        file.write(f"____________\n")
        note = notes[i]
        b = 0
        for key, values in note.items():
            file.write(f"{key_ru[b]}: {values}\n")
            b += 1
        file.write(f"______________________\n")
    file.close()
if __name__ == "__main__":
     save_notes_to_file(notes, filename)