import pytest

from src.pre_built.counter import count_ocurrences


def test_counter():
    expected_counter_list = [122, 1639]
    results = count_ocurrences("data/jobs.csv", 'javascript')
    assert type(results) is int
    assert results == expected_counter_list[0]

    results = count_ocurrences("data/jobs.csv", 'JAVASCRIPT')
    assert results == expected_counter_list[0]

    results = count_ocurrences("data/jobs.csv", 'python')
    assert results == expected_counter_list[1]

    with pytest.raises(FileNotFoundError):
        count_ocurrences("um_arquivo_que_não_existe.csv", 'word')
