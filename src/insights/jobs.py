import csv
from functools import lru_cache
from typing import Dict, List


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, 'r', encoding="utf-8") as f:
        jobs = csv.DictReader(f, delimiter=',')
        headers, *rows = jobs
        jobs_data = [headers, *rows]
        return jobs_data


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    job_types = [job['job_type'] for job in data]
    return list(set(job_types))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
