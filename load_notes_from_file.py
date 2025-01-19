import yaml
import os
from fileinput import filename
def load_notes_from_file(filename):
    if os.path.isfile("filename.yaml"):
        with open('filename.yaml', 'r', encoding='utf-8') as file:
            notes = yaml.safe_load(file)
        file.close()
        if notes == None:
            print('Список заметок пуст')
        else:
            print('Все заметки:')
            for i in range(len(notes)):
                print('Заметка №', i + 1)
                note = notes[i]
                for key, values in note.items():
                    print(key, ':', values)
                print('_____________________')
        return notes
    else:
        print("Файл не существует")
if __name__ == "__main__":
    load_notes_from_file(filename)
