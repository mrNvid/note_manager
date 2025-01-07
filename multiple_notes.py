notes = []
note = {}
print("Менеджер заметок")
print("Вы можете добавить новую заметку:")
while True:
    name = input('Введите имя:')
    note['Имя'] = name
    title = input('Введите заголовок заметки:')
    note['Заголовок'] = title
    content = input('Введите текст заметки:')
    note['Описание'] = content
    status = input('Введите статус заметки:')
    note['Статус'] = status
    created_date = input('Введите дату создания заметки в формате день-месяц-год:')
    note['Дата создания'] = created_date
    issue_date = input('Введите дату истечения заметки в формате день-месяц-год:')
    note['Дедлайн'] = issue_date
    notes.append(note)
    new_note = input("Хотите добавить ещё одну заметку? (да/нет)")
    if new_note == "нет":
        break
for x, y in notes[1].items():
    print(x,':', y)