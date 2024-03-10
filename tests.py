import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.mark.parametrize(
        'title',
        [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить']
    )
    def test_add_new_book_add_correct_title_book_added(self, title):
        collector = BooksCollector()

        collector.add_new_book(title)
        assert title in collector.get_books_genre()

    @pytest.mark.parametrize(
        'title',
        ['Жизнь, необыкновенные и удивительные приключения Робинзона Крузо, моряка из Йорка, прожившего двадцать восемь лет в полном одиночестве на необитаемом острове у берегов Америки близ устьев реки Ориноко, куда он был выброшен кораблекрушением, во время которого весь экипаж корабля, кроме него, погиб, с изложением его неожиданного освобождения пиратами; написанные им самим',
        '']
        )
    def test_add_new_book_wrong_len_title_book_not_added(self, title):
        collector = BooksCollector()

        collector.add_new_book(title)
        assert title not in collector.get_books_genre()

    def test_set_book_genre_title_in_list_and_correct_genre_genre_set(self):
        collector = BooksCollector()

        collector.add_new_book('Истина Кхорна')
        collector.set_book_genre('Истина Кхорна', 'Фантастика')

        assert collector.get_book_genre('Истина Кхорна') == 'Фантастика'

    def test_set_book_genre_title_in_list_and_incorrect_genre_genre_not_set(self):
        collector = BooksCollector()

        collector.add_new_book('Наука Плоского мира')
        collector.set_book_genre('Наука Плоского мира', 'Фэнтези')

        assert not collector.get_book_genre('Наука Плоского мира') == 'Фэнтези'

    def test_get_book_genre_book_in_list_return_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Истина Кхорна')
        collector.set_book_genre('Истина Кхорна', 'Фантастика')
        assert collector.get_book_genre('Истина Кхорна') in 'Фантастика'

    def test_get_book_genre_book_in_list_without_genre_genre_not_set(self):
        collector = BooksCollector()

        collector.add_new_book('Наука Плоского мира')
        collector.set_book_genre('Наука Плоского мира', 'Фэнтези')
        assert collector.get_book_genre('Наука Плоского мира') is ''

    def test_get_book_genre_book_not_in_list_no_book_no_genre(self):
        collector = BooksCollector()

        assert collector.get_book_genre('Эпос о Гильгамеше') is None

    def test_get_books_with_specific_genre_book_with_specific_genre_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Истина Кхорна')
        collector.set_book_genre('Истина Кхорна', 'Фантастика')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 1

    def test_get_books_with_specific_genre_book_without_specific_genre_zero_books(self):
        collector = BooksCollector()

        collector.add_new_book('Истина Кхорна')
        collector.set_book_genre('Истина Кхорна', 'Фантастика')
        assert len(collector.get_books_with_specific_genre('Детективы')) == 0

    @pytest.mark.parametrize(
        'title,genre',
        [
            ['Истина Кхорна', 'Фантастика'],
            ['Молчание ягнят', 'Детективы']
         ]
    )
    def test_get_books_genre_book_with_correct_title_get_genre_of_book(self, title, genre):
        collector = BooksCollector()

        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert collector.get_book_genre(title) == genre

    def test_get_books_for_children_age_rating_book_zero_books(self):
        collector = BooksCollector()

        collector.add_new_book('Хребты безумия')
        collector.set_book_genre('Хребты безумия', 'Ужасы')
        assert len(collector.get_books_for_children()) == 0

    def test_get_books_for_children_no_age_rating_book_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Шляпа, полная неба')
        collector.set_book_genre('Шляпа, полная неба', 'Фантастика')
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_title_in_list_one_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Благие знамения')
        collector.add_book_in_favorites('Благие знамения')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_title_not_in_list_zero_in_favorites(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Благие знамения')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_title_is_one_of_two_favorites_one_favorite(self):
        collector = BooksCollector()

        collector.add_new_book('Благие знамения')
        collector.add_book_in_favorites('Благие знамения')
        collector.add_new_book('Прогнивший Трон')
        collector.add_book_in_favorites('Прогнивший Трон')
        collector.delete_book_from_favorites('Прогнивший Трон')
        assert len(collector.get_list_of_favorites_books()) == 1

    @pytest.mark.parametrize(
        'title',
        ['Истина Кхорна', 'Молчание ягнят']
    )
    def test_get_list_of_favorites_books_one_book_from_list_added_one_favorite(self, title):
        collector = BooksCollector()

        collector.add_new_book(title)
        collector.add_book_in_favorites(title)
        assert len(collector.get_list_of_favorites_books()) == 1























