from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salary = 0
    for job in data:
        if job["max_salary"].isnumeric():
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salary = get_max_salary(path)
    for job in data:
        if job["min_salary"].isnumeric():
            if int(job["min_salary"]) < min_salary:
                min_salary = int(job["min_salary"])
    print(min_salary)
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Job doesn't have min_salary or max_salary")

    if not str(salary).lstrip("-").isnumeric():
        raise ValueError("Salary isn't a valid integer")

    if not str(job["min_salary"]).isnumeric():
        raise ValueError("Job min_salary isn't a valid integer")

    if not str(job["max_salary"]).isnumeric():
        raise ValueError("Job max_salary isn't a valid integer")

    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("Job min_salary is greater than max_salary")

    if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
        return True
    else:
        return False


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
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass
    return filtered_jobs
