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
