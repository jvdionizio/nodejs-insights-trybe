from src.pre_built.counter import count_ocurrences

path = "data/jobs.csv"


def test_counter():

    assert count_ocurrences(path, "Python") == 1639
    assert count_ocurrences(path, "Javascript") == 122
