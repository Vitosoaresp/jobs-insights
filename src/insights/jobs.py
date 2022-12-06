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
    jobs_by_job_type = [job for job in jobs if job['job_type'] == job_type]
    return jobs_by_job_type
