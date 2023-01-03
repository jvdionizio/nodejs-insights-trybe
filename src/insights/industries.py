from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    industries_list = []
    for job in data:
        if job["industry"] not in industries_list:
            if job["industry"] != "":
                industries_list.append(job["industry"])
    return industries_list


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)
    return filtered_jobs
