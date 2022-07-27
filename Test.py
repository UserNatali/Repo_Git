def my_teacher():
    teach = {"Петренко Микола Іванович": "10А", "Іванченко Світлана Вікторівна": "9В", "Красовський Богдан Юрійович":
             "8А"}
    print(teach)


def my_timetable():
    timetable = {"1": "9.00-9.45", "2": "9.55-10.40", "3": "10.50-11.35", "4": "11.45-12.30"}
    print(timetable)


def my_library():
    library = {"Панас МирнийПанас Мирний": "Хіба ревуть воли як ясла повні", "Іван Франко": "Захар Беркут",
               "Леся Українка": "Лісова Пісня"}

    while True:
        choice = input("10.Додати автора з книгою\n20.Видалити автора з книгою\n30.Вихід\n")
        if choice == "30":
            break
        elif choice == "10":
            author = input("Введіть автора: ")
            book = input("Введіть назву книги: ")
            library[author] = book
            print(library)
        elif choice == "20":
            author_del = input("Введіть автора: ")
            if author_del in library:
                library.pop(author_del)
                print(library)
            else:
                print("Книги з таким автором в бібліотеці нема")
        else:
            print("Неправильний вибір")


def my_menu():
    while True:
        print("Меню.\n1.Інформація про викладачів.\n2.Інформація про розклад дзвінків.\n3.Бібліотека.\n4.Вихід")
        number = input("number = ")
        if number == "1":
            my_teacher()
        elif number == "2":
            my_timetable()
        elif number == "3":
            my_library()
        elif number == "4":
            break
        else:
            print("Неправильний вибір")


my_menu()
