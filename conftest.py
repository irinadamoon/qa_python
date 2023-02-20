import pytest
from main import BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def addition(collector):
    collector = collector.add_new_book('Гордость и предубеждение и зомби')
    return collector

@pytest.fixture
def favorite(collector):
    collector = collector.add_book_in_favorites('Гордость и предубеждение и зомби')
    return collector



    
    
