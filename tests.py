import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        'title',
        ['Жизнь, необыкновенные и удивительные приключения Робинзона Крузо, моряка из Йорка, прожившего двадцать восемь лет в полном одиночестве на необитаемом острове у берегов Америки близ устьев реки Ориноко, куда он был выброшен кораблекрушением, во время которого весь экипаж корабля, кроме него, погиб, с изложением его неожиданного освобождения пиратами; написанные им самим',
        '']
        )
    def test_add_new_book_wrong_len_title_zero_books(self, title):
        collector = BooksCollector()

        collector.add_new_book(title)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_title_in_list_and_correct_genre_genre_set(self):
        collector = BooksCollector()

        collector.add_new_book('Истина Кхорна')
        collector.set_book_genre('Истина Кхорна', 'Фантастика')
        assert 'Истина Кхорна' in collector.books_genre.keys() and 'Фантастика' in collector.books_genre.values()

    def test_set_book_genre_title_in_list_and_incorrect_genre_genre_not_set(self):
        collector = BooksCollector()

        collector.add_new_book('Наука Плоского мира')
        collector.set_book_genre('Наука Плоского мира', 'Фэнтези')
        assert 'Наука Плоского мира' in collector.books_genre.keys() and 'Фэнтези' not in collector.books_genre.values()

    def test_set_book_genre_title_not_in_list_and_correct_genre_genre_and_title_not_set(self):
        collector = BooksCollector()

        collector.set_book_genre('Молчание ягнят', 'Детективы')
        assert 'Молчание ягнят' not in collector.books_genre.keys() and 'Детективы' not in collector.books_genre.values()

    def test_get_book_genre_book_in_list_return_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Истина Кхорна')
        collector.set_book_genre('Истина Кхорна', 'Фантастика')
        assert collector.get_book_genre('Истина Кхорна') in 'Фантастика'

    def test_get_book_genre_book_in_list_without_genre_no_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Наука Плоского мира')
        collector.set_book_genre('Наука Плоского мира', 'Фэнтези')
        assert collector.get_book_genre('Наука Плоского мира') is ''

    def test_get_book_genre_book_not_in_list_no_genre(self):
        collector = BooksCollector()

        assert collector.get_book_genre('Эпос о Гильгамеше') is None

    def test_get_books_with_specific_genre_book_with_specific_genre_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Истина Кхорна')
        collector.set_book_genre('Истина Кхорна', 'Фантастика')
        books_with_specific_genre = collector.get_books_with_specific_genre('Фантастика')
        assert len(books_with_specific_genre) == 1

    def test_get_books_with_specific_genre_book_withot_specific_genre_no_books(self):
        collector = BooksCollector()

        collector.add_new_book('Истина Кхорна')
        collector.set_book_genre('Истина Кхорна', 'Фантастика')
        books_with_specific_genre = collector.get_books_with_specific_genre('Детективы')
        assert len(books_with_specific_genre) == 0

    @pytest.mark.parametrize(
        'title,genre',
        [
            ['Истина Кхорна', 'Фантастика'],
            ['Эпос о Гильгамеше', 'Эпос']
         ]
    )
    def test_get_books_genre_book_with_correct_title_get_one_book(self, title, genre):
        collector = BooksCollector()

        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        books_genre = collector.get_books_genre()
        assert len(books_genre) == 1

    @pytest.mark.parametrize(
        'title,genre',
        [
            [
                'Волшебный двурог, или Правдивая история небывалых приключений нашего отважного друга Ильи Алексеевича Комова в неведомой стране, где правят: Догадка, Усидчивость, Находчивость, Терпение, Остроумие и Трудолюбие, и которая в то же время есть пресветлое царство веселого, но совершенно таинственного существа, чье имя очень похоже на название этой удивительной книжки, которую подлежит читать не торопясь',
                'Фантастика'],
            ['', '']
        ]
    )
    def test_get_books_genre_book_with_incorrect_titles_zero_books(self, title, genre):
        collector = BooksCollector()

        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        books_genre = collector.get_books_genre()
        assert len(books_genre) == 0

    def test_get_books_for_children_age_rating_book_zero_books(self):
        collector = BooksCollector()

        collector.add_new_book('Хребты безумия')
        collector.set_book_genre('Хребты безумия', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 0

    def test_get_books_for_children_no_age_rating_book_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Шляпа, полная неба')
        collector.set_book_genre('Шляпа, полная неба', 'Фантастика')
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 1

    def test_add_book_in_favorites_title_in_list_one_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Благие знамения')
        collector.set_book_genre('Благие знамения', 'Фантастика')
        collector.add_book_in_favorites('Благие знамения')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_title_not_in_list_zero_in_favorites(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Благие знамения')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_title_is_one_of_two_favorites_one_favorite(self):
        collector = BooksCollector()

        collector.add_new_book('Благие знамения')
        collector.set_book_genre('Благие знамения', 'Фантастика')
        collector.add_book_in_favorites('Благие знамения')
        collector.add_new_book('Прогнивший Трон')
        collector.set_book_genre('Прогнивший Трон', 'Фантастика')
        collector.add_book_in_favorites('Прогнивший Трон')
        collector.delete_book_from_favorites('Прогнивший Трон')
        assert len(collector.get_list_of_favorites_books()) == 1

    @pytest.mark.parametrize(
        'title,genre',
        [
            ['Истина Кхорна', 'Фантастика'],
            ['Эпос о Гильгамеше', 'Эпос']
        ]
    )
    def test_get_list_of_favorites_books_one_book_from_list_added_one_favorite(self, title, genre):
        collector = BooksCollector()

        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        collector.add_book_in_favorites(title)
        assert len(collector.get_list_of_favorites_books()) == 1























