import pytest
from people import Person


@pytest.fixture()
def con():
    return None


@pytest.fixture()
def person():
    print("\nPrint!!!!")
    return Person(name="Bob", age=1)


def test_person(person, con):
    print("\ntest first")
    person.get_older(10)
    assert person.age == 11


def test_second(person):
    print("\ntest second")
    res = sum([1, 0, 0, 0])
    assert res == 1

