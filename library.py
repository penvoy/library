import json
import os 


class Book:
    """Класс для представления книги."""

    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Преобразует объект книги в словарь для хранения в JSON."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }


class Library:
    """Класс для управления библиотекой книг."""

    def __init__(self, filename: str):
        self.books = []
        self.filename = filename
        self.load_books()

    def load_books(self):
        """Загружает книги из файла."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                books_data = json.load(f)
                self.books = [Book(**data) for data in books_data]

    def save_books(self):
        """Сохраняет книги в файл."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([book.to_dict() for book in self.books],
                      f, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """Добавляет книгу в библиотеку."""
        # генерируем id
        book_id = len(self.books) + 1
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, book_id: int):
        """Удаляет книгу из библиотеки по ID."""
        for book in self.books:
            if book.id == book_id:
                # убираем
                self.books.remove(book)
                # сохраняем изменения
                self.save_books()
                return
        raise ValueError(f"Книга с ID {book_id} не найдена.")

    def search_books(self, search_term: str):
        """Ищет книги по заголовку, автору или году."""
        results = [
            book for book in self.books if search_term in book.title or search_term in book.author or search_term == str(book.year)]
        return results

    def display_books(self):
        """Отображает все книги в библиотеке."""
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books:
            print(
                f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    def change_status(self, book_id: int, new_status: str):
        """Изменяет статус книги по ID."""
        if new_status not in {"в наличии", "выдана"}:
            raise ValueError("Статус должен быть 'в наличии' или 'выдана'.")
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                self.save_books()
                return
        raise ValueError(f"Книга с ID {book_id} не найдена.")
