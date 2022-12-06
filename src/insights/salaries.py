from typing import Dict, List, Union

from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_data = read(path)
    max_salary = 0
    for job in jobs_data:
        if job['max_salary'] == 'invalid' or job['max_salary'] == '':
            continue
        elif int(float(job['max_salary'])) > max_salary:
            max_salary = int(float(job['max_salary']))
    return max_salary


def get_min_salary(path: str) -> int:
    jobs_data = read(path)
    new_jobs_data = [
                        job for job in jobs_data
                        if job['min_salary'] != 'invalid'
                        and job['min_salary'] != ''
                    ]
    min_salary = int(float(new_jobs_data[0]['min_salary']))
    for job in new_jobs_data:
        min_salary = min(int(float(job['min_salary'])), min_salary)
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError()
    min: Union[int, str] = job['min_salary']
    max: Union[int, str] = job['max_salary']
    if (
        type(salary) == str and salary.isnumeric() or type(salary) == int
    ) and (
        type(min) == str and min.isnumeric() or type(min) == int
    ) and (
        type(max) == str and max.isnumeric() or type(max) == int
    ):
        salary = int(salary)
        min = int(min)
        max = int(max)
        if (min > max):
            raise ValueError()
        return salary >= min and salary <= max
    else:
        raise ValueError()


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
