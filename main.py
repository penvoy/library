from library import Library


def main():
    library = Library("books.json")

    while True:
        print("\n1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книги")
        print("4. Отображать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        try:
            if choice == '1':
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год издания книги: "))
                library.add_book(title, author, year)

            elif choice == '2':
                book_id = int(input("Введите ID книги, которую нужно удалить: "))
                library.remove_book(book_id)

            elif choice == '3':
                search_term = input("Введите заголовок, автора или год для поиска: ")
                results = library.search_books(search_term)
                if results:
                    for book in results:
                        print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
                else:
                    print("Книги не найдены.")

            elif choice == '4':
                library.display_books()

            elif choice == '5':
                book_id = int(input("Введите ID книги для изменения статуса: "))
                new_status = input("Введите новый статус (в наличии/выдана): ")
                library.change_status(book_id, new_status)

            elif choice == '6':
                break

            else:
                print("Неверный выбор, попробуйте снова.")

        except ValueError as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()