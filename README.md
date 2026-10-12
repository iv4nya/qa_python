# class TestBooksCollector

## Реализованные в классе тесты

1. test_add_new_book_add_one_book - проверяет добавление одной книги в словарь

2. test_add_new_book_with_len_41 - проверяет не добавление книги в словарь если длина названия > 41 символа

3. test_add_new_book_twice - проверяет, что нельзя добавить книгу дважды

4. test_set_book_genre_name_not_in_genre - проверяет, что жанр для книги не устанавливается, если жанра нет в списке genre

5. test_get_book_genre_returns_all_genres - проверяет, что метод возвращает все жанры

6. test_get_books_with_specific_genre_returns_books - проверяет, что метод возвращает название книги по жанру

7. test_get_books_genre_returns_dictionary - проверяет, что метод возвращает словарь books_genre

8. test_get_books_for_children_dont_return_adult_genre - проверяет, что метод возвращает только те книги, которые есть в списке genre, но нет в списке genre_age_rating

9. test_add_book_in_favorites_dont_add_book_twice - проверяет, что метод не добавляет название книги в список favorites дважды

10. test_delete_book_from_favorites_delete_book_from_favorites - проверяет, что метод удаляет книгу из списка favorites

11. test_get_list_of_favorites_books_return_favorites - проверяет, что метод возвращает список favorites

