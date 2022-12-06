from typing import Dict, List

from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_data = read(path)
    sum_jobs_by_industry = {}
    for job in jobs_data:
        if job['industry'] == '':
            continue
        elif job['industry'] in sum_jobs_by_industry:
            sum_jobs_by_industry[job['industry']] += 1
        else:
            sum_jobs_by_industry[job['industry']] = 1
    return sum_jobs_by_industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobs_filter_industry = [job for job in jobs if job['industry'] == industry]
    return jobs_filter_industry
