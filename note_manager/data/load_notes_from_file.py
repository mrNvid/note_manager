import os
from fileinput import filename
def load_notes_from_file(filename):
    notes_ru = []
    notes = []
    try:
        with open('filename', 'r', encoding='utf-8') as file:
            content = file.read()
        if content:
            note_blocks = content.split('\n---\n')
            for block in note_blocks:
                if block != '':
                    note_lines = block.split('\n')
                    note = {}
                    for line in note_lines:
                        key, value = line.split(': ', 1)
                        note[key.strip()] = value
                    notes_ru.append(note)
            key_eu = ['username', 'title', 'content', 'status', 'issue_date', 'created_date']
        for i in range(len(notes_ru)):
            note = notes_ru[i]
            note = dict(zip(key_eu, list(note.values())))
            notes.append(note)
        return notes

    except FileNotFoundError:
        notes = open('filename', 'w+')
        notes.close()
        print("Файл не найден. Создан новый файл")
    except UnicodeDecodeError:
        print('Не удалось декодировать файл')
    except PermissionError:
        print('Ошибка доступа')
    except Exception:
        print('Непредвиденная ошибка')
if __name__ == "__main__":
    notes = load_notes_from_file(filename)
    print('Все заметки:')
    for i in range(len(notes)):
        print('Заметка №', i + 1)
        note = notes[i]
        for key, values in note.items():
            print(key, ':', values)
        print('_____________________')
