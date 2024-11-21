# Библиотечное приложение

Это консольное приложение для управления библиотекой книг. Оно позволяет добавлять, удалять, искать и отображать книги, а также изменять их статус.

## Установка и использование

1. Скачайте или клонируйте репозиторий.
2. Убедитесь, что у вас установлен Python 3.
3. Перейдите в папку app.
4. Запустите приложение с помощью команды:
   ```
   python main.py
   ```

## Функционал

- **Добавление книги**: Вводите название, автора и год издания.
- **Удаление книги**: Укажите ID книги для удаления.
- **Поиск книги**: Ищите по названию, автору или году издания.
- **Отображение всех книг**: Показать все книги с их данными.
- **Изменение статуса книги**: Укажите новый статус (`в наличии` или `выдана`).

## Формат хранения данных

Данные о книгах хранятся в файле `books.json` в формате JSON.
