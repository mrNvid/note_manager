def create_note():
    print('Создание заметки!')
    print('Заметка создана!')
def display_notes():
    print('Отображение всех заметок')
def update_note():
    print('Обновление заметки')
def delete_note():
    print('Удаление заметки')
def search_notes():
    print('Поиск заметки')

print('Добро пожаловать в менеджер заметок!')
while True:
    print('Выберете одно из доступных действий меню.')
    print('________________________________________')
    print('Меню действий:')
    print('1. Создать новую заметку')
    print('2. Показать все заметки')
    print('3. Обновить заметку')
    print('3. Обновить заметку')
    print('3. Обновить заметку')
    print('6. Выйти из программы')
    print('________________________________________')
    user_input = input('Введите номер действия:')
    print('Ваш выбор:', user_input)
    print('________________________________________')
    if user_input == '1':
        create_note()
    elif user_input == '2':
        display_notes()
    elif user_input =='3':
        update_note()
    elif user_input =='4':
        delete_note()
    elif user_input =='5':
        search_notes()
    elif user_input =='6':
        print('Программа завершена. Спасибо за использование!')
        break
    else: print('Ошибка ввода, попробуйте снова')