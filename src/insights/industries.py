from typing import List, Dict
from jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    industries_list = []
    for job in data:
        if job["industry"] not in industries_list:
            if job["industry"] != "":
                industries_list.append(job["industry"])
    print(industries_list)
    return industries_list


get_unique_industries("data/jobs.csv")


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
