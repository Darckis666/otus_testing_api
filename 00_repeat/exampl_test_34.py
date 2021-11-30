import pytest


def foo():
    pass


@pytest.fixture()
def a():
    pass


@pytest.fixture()
def b():
    pass


def test_exampl_1(a, b):
    pass


class TestClass:

    def test_2(self):
        pass
