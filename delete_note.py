notes = [{'Имя': 'Никита','Заголовок': 'Покупки','Описание': 'Купить картошку'},
         {'Имя': 'Ирина','Заголовок': 'Учёба','Описание': 'Сделать реферат'},
         {'Имя': 'Полина','Заголовок': 'Работа','Описание': 'Сдать смену'}]
coincidences = 0
print('Все заметки:')
for i in range(len(notes)):
    print('_____________________')
    note = notes[i]
    for key, values in note.items():
        print(key,':', values)
condition_del = input('Введите имя пользователя или заголовок для удаления заметки:')
if len(notes) == 0:
    print('Список заметок пуст!')
else:
    for i in range(len('Имя')):
        note = notes[i]
        if condition_del.lower() == note['Имя'].lower() or condition_del.lower() == note['Заголовок'].lower():
            del notes[i]
            coincidences = 1
            break
    if coincidences == 1:
        print('-----------------------')
        print('Успешно удалено. Остались следующие заметки:')
        for i in range(len(notes)):
            print('_____________________')
            note = notes[i]
            for key, values in note.items():
                print(key, ':', values)
    else: print('Заметок с таким именем пользователя или заголовком не найдено.')