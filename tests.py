import pytest
from main import BooksCollector

@pytest.fixture()
def collector():
    return BooksCollector()

class TestBooksCollector:

    def test_add_new_book_add_one_book(self, collector):

        collector.add_new_book('Бойцовский клуб')
        assert 'Бойцовский клуб' in collector.books_genre

    def test_add_new_book_with_len_41(self, collector):

        collector.add_new_book('Интереснейшая книга из 41 символа 12345678')
        assert 'Интереснейшая книга из 41 символа 12345678' not in collector.books_genre

    def test_add_new_book_twice(self, collector):

        collector.add_new_book('Колобок')
        collector.add_new_book('Колобок')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_name_not_in_genre(self, collector):

        genre = 'Триллер'
        name = 'Атака титанов'

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == ''

    @pytest.mark.parametrize(
            'genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    )
    def test_get_book_genre_returns_all_genres(self, collector, genre):

        collector.add_new_book('Невероятная комедия')
        collector.set_book_genre('Невероятная комедия', genre)
        assert collector.get_book_genre('Невероятная комедия') == genre

    def test_get_books_with_specific_genre_returns_books(self, collector):

        collector.add_new_book('Паладины')
        collector.add_new_book('Ромком')
        collector.set_book_genre('Паладины', 'Комедии')
        collector.set_book_genre('Ромком', 'Ужасы')
        
        assert collector.get_books_with_specific_genre('Ужасы') == ['Ромком']

    def test_get_books_genre_returns_dictionary(self, collector):

        collector.add_new_book('Паладины')
        collector.add_new_book('Ромком')
        collector.set_book_genre('Паладины', 'Комедии')
        collector.set_book_genre('Ромком', 'Ужасы')

        assert collector.get_books_genre() == {'Паладины': 'Комедии',
                                                'Ромком': 'Ужасы'
                                                }

    def test_get_books_for_children_dont_return_adult_genre(self, collector):

        collector.add_new_book('Паладины')
        collector.add_new_book('Ромком')
        collector.set_book_genre('Паладины', 'Комедии')
        collector.set_book_genre('Ромком', 'Ужасы')

        assert collector.get_books_for_children() == ['Паладины']

    def test_add_book_in_favorites_dont_add_book_twice(self, collector):

        collector.add_new_book('Паладины')
        collector.add_new_book('Ромком')
        collector.set_book_genre('Паладины', 'Комедии')
        collector.set_book_genre('Ромком', 'Ужасы')
        collector.add_book_in_favorites('Паладины')
        collector.add_book_in_favorites('Паладины')

        assert collector.favorites == ['Паладины']

    def test_delete_book_from_favorites_delete_book_from_favorites(self, collector):

        collector.add_new_book('Паладины')
        collector.add_book_in_favorites('Паладины')
        collector.delete_book_from_favorites('Паладины')

        assert collector.favorites == []

    def test_get_list_of_favorites_books_return_favorites(self, collector):

        collector.add_new_book('Паладины')
        collector.add_book_in_favorites('Паладины')

        assert collector.get_list_of_favorites_books() == ['Паладины']