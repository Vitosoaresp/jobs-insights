import pytest

from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    expected_keys = ["title", "salary", "type"]

    result = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert type(result) == list
    assert len(result) == 15

    for job in result:
        assert type(job) == dict
        for keys in expected_keys:
            assert keys in job
            assert "titulo" not in job
            assert "salario" not in job
            assert "tipo" not in job

    with pytest.raises(FileNotFoundError):
        read_brazilian_file("um_arquivo_que_não_existe.csv")
