from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, file_path: str) -> List[Dict]:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.jobs_list.append(row)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set()
        for job in self.jobs_list:
            job_type = job.get('job_type')
            if job_type:
                unique_job_types.add(job_type)
        return list(unique_job_types)

    def filter_by_multiple_criteria(self, jobs: List[Dict], filter_criteria: Dict) -> List[Dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError('filter_criteria must be a dictionary')
        
        filtered_jobs = list()
        for job in jobs:
            if all(job.get(key) == value for key, value in filter_criteria.items()):
                filtered_jobs.append(job)
        return filtered_jobs

