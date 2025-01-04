username = input('Введите имя:')
title_list = []
title_list.append(input('Введите Заголовок:'))
title_list.append(input('Введите второй заголовок:'))
title_list.append(input('Введите третий заголовок:'))
content = input('Введите текст заметки:')
status = input('Введите статус заметки:')
created_date = input('Введите дату создания заметки в формате день.месяц.год:')
issue_date = input('Введите дату истечения заметки в формате день.месяц.год:')
note = {"Имя пользователя": username,"Содержание заметки" : content,"Статус" : status,
              "Дата создания" : created_date,"Дата изменения" : issue_date, "Заголовки" : title_list}
print(note)