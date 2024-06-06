from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = None
        for job in self.jobs_list:
            if job.get('max_salary') and job['max_salary'].isdigit():
                salary = int(job['max_salary'])
                max_salary = (
                    max(max_salary, salary)
                    if max_salary is not None
                    else salary
                )
        return max_salary

    def get_min_salary(self) -> int:
        min_salary = None
        for job in self.jobs_list:
            if job.get('min_salary') and job['min_salary'].isdigit():
                salary = int(job['min_salary'])
                min_salary = (
                    min(min_salary, salary)
                    if min_salary is not None
                    else salary
                )
        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if 'min_salary' not in job or 'max_salary' not in job:
            raise ValueError('Job does not have salary information')
        try:
            min_salary = int(job['min_salary'])
            max_salary = int(job['max_salary'])
            mid_salary = float(salary)
        except (ValueError, TypeError):
            raise ValueError('Salary information is not valid')
        if min_salary > max_salary:
            raise ValueError(
                'Minimum salary cannot be greater than maximum salary'
            )
        return min_salary <= mid_salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
