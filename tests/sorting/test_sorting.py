import pytest

from src.pre_built.sorting import sort_by

fake_jobs = [
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2022-12-07"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2022-12-08"},
    {"max_salary": 1900, "min_salary": 100, "date_posted": "2022-12-06"},
]


def test_sort_by_criteria():
    expect_results = {
        "max_salary": [
            {
                "max_salary": 10000,
                "min_salary": 200,
                "date_posted": "2022-12-07",
            },
            {
                "max_salary": 1900,
                "min_salary": 100,
                "date_posted": "2022-12-06",
            },
            {"max_salary": 1500, "min_salary": 0, "date_posted": "2022-12-08"},
        ],
        "min_salary": [
            {"max_salary": 1500, "min_salary": 0, "date_posted": "2022-12-08"},
            {
                "max_salary": 1900,
                "min_salary": 100,
                "date_posted": "2022-12-06",
            },
            {
                "max_salary": 10000,
                "min_salary": 200,
                "date_posted": "2022-12-07",
            },
        ],
        "date_posted": [
            {"max_salary": 1500, "min_salary": 0, "date_posted": "2022-12-08"},
            {
                "max_salary": 10000,
                "min_salary": 200,
                "date_posted": "2022-12-07",
            },
            {
                "max_salary": 1900,
                "min_salary": 100,
                "date_posted": "2022-12-06",
            },
        ],
    }

    keys_criteria = ["max_salary", "min_salary", "date_posted"]
    for keys in keys_criteria:
        sort_by(fake_jobs, keys)
        assert fake_jobs == expect_results[keys]

    with pytest.raises(
        ValueError, match="invalid sorting criteria: chave errada"
    ):
        sort_by(fake_jobs, "chave errada")
