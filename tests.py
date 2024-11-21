import unittest
import os
from unittest.mock import patch
import io

from library import Library, Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Создаем временный файл для тестов"""
        self.library = Library('test_library.json')
        self.library.books = []  # Очищаем библиотеку для тестов

    def tearDown(self):
        """Удаляем временный файл после тестов"""
        if os.path.exists('test_library.json'):
            os.remove('test_library.json')

    def test_add_book(self):
        """Тестируем добавление книги"""
        self.library.add_book('Test Book', 'Author', 2021)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, 'Test Book')

    def test_remove_book(self):
        """Тестируем удаление книги"""
        self.library.add_book('Test Book', 'Author', 2021)
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 0)

    def test_find_book_by_title(self):
        """Тестируем поиск книги по заголовку"""
        self.library.add_book('Test Book', 'Author', 2021)
        self.library.add_book('Another Book', 'Another Author', 2022)
        
        found_books = self.library.search_books('Test Book')
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0].title, 'Test Book')

    def test_change_status(self):
        """Тестируем изменение статуса книги"""
        self.library.add_book('Test Book', 'Author', 2021)
        self.library.change_status(1, 'выдана')
        
        self.assertEqual(self.library.books[0].status, 'выдана')

    def test_display_books(self):
        """Тестируем отображение книг"""
        self.library.add_book('Test Book', 'Author', 2021)
        
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.library.display_books()
            output = fake_out.getvalue()

        # Проверяем, что вывод содержит название книги
        self.assertIn('Test Book', output)

if __name__ == '__main__':
    unittest.main()