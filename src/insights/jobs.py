from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as job_csv_file:
        data = csv.DictReader(job_csv_file)
        return list(data)


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    job_types_list = []
    for job in data:
        if job["job_type"] not in job_types_list:
            job_types_list.append(job["job_type"])
    return job_types_list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    job_type_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_type_list.append(job)
    return job_type_list
