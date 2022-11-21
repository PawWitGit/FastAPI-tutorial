from typing import Optional
from typing import List


class Job:
    def __init__(self, title: str, description: Optional[str]) -> None:
        self.title = title
        self.description = description

    def __repr__(self):
        return self.title


job1 = Job(title="SDE2", description="Sdfdk")
job2 = Job(title="Senior Manager", description="jfjdj")

jobs: List[Job] = [job1, job2]

print(jobs)
