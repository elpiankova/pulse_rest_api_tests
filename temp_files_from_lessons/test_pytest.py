V = 100

def setup_module(m):
    connection = 100
    print("\nSet up module", m)


def setup():
    connection = 100
    print("\nSet up")


def teardown_function(func):
    print("\nTeardown up", func)


def test_first():
    print("\ntest first")
    res = sum([1, 2, 4, 5])
    assert res == 12
    assert res + 1 == 13


def test_second():
    print("\ntest second")
    res = sum([1, 0, 0, 0])
    assert res == 1

