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

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
