from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

# Мои попытки тестов

# проверить что рейтинг по умолчанию 1
    def test_add_new_book_rating_1(self, collector, addition):
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

# установили рейтинг 1_5_10 вместо 1 по умолчанию
    import pytest
    @pytest.mark.parametrize('num', [1, 5, 10])
    def test_set_book_rating_1_5_10(self, collector, addition, num):
        collector.set_book_rating('Гордость и предубеждение и зомби', num)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == num

# что что-то получаем на запрос рейтинга книги по имени
    def test_get_book_rating(self, collector, addition):
        assert collector.get_book_rating('Гордость и предубеждение и зомби')

# список книг с корректным рейтингом 5
    def test_get_books_with_specific_rating_5(self, collector, addition):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        assert collector.get_books_with_specific_rating(5) == ['Гордость и предубеждение и зомби']

# получаем именно словарь, а не строку
    def test_get_books_rating(self, collector, addition):
        assert type(collector.get_books_rating()) is dict

# книга добавилась в избранное
    def test_add_book_in_favorites_book_added(self, collector, addition, favorite):
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

# книга удалилась из избранного
    def test_delete_book_from_favorites_book_delited(self, collector, addition, favorite):
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

# получили список избранных книг
    def test_get_list_of_favorites_books(self, collector, addition, favorite):
        assert len(collector.get_list_of_favorites_books()) > 0

# удаление несуществующей книги не привело к удалению других
    def test_delete_book_from_favorites_non_existed_book(self, collector, addition, favorite):
        collector.delete_book_from_favorites('Незнайка на Луне')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

# установить рейтинг выше 10 невозможно
    def test_test_set_book_rating_set_rating_15_is_not_possible(self, collector, addition):
        assert collector.set_book_rating('Гордость и предубеждение и зомби', 15) == None

# при запросе книг с несуществ рейтингом вернется пустой список
    def test_get_books_with_specific_rating_returns_empty_list_if_rating15(self, collector, addition):
        assert collector.get_books_with_specific_rating(15) == []

