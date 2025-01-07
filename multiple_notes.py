notes = []
note = {}
print("Менеджер заметок")
print("Вы можете добавить новую заметку:")
while True:
    name = input('Введите имя:')
    title = input('Введите заголовок заметки:')
    content = input('Введите текст заметки:')
    status = input('Введите статус заметки:')
    created_date = input('Введите дату создания заметки в формате день-месяц-год:')
    issue_date = input('Введите дату истечения заметки в формате день-месяц-год:')
    note.update({'Имя': name, 'Заголовок' : title, 'Описание' : content, 'Статус': status, 'Дата создания': created_date,'Дедлайн': issue_date},)
    notes.append(note)
    note.clear()
    new_note = input("Хотите добавить ещё одну заметку? (да/нет)")
    if new_note == "нет":
        break
print('Все заметки:')
а=0
while True:
    for x, y in notes:
        print(x,':', y)
        а=а+1
        break