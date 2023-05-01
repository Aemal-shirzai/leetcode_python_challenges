from typing import List

class Solution:
    def average(self, salary: List[int]):
        salary.remove(min(salary))
        salary.remove(max(salary))
        return sum(salary) / len(salary)