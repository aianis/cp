class Solution:
    def average(self, salary: List[int]) -> float:
        # Calculate the sum of salaries excluding the minimum and maximum salary
        sum_salary = sum(salary) - min(salary) - max(salary)
        # Calculate the count of employees excluding the minimum and maximum salary
        count = len(salary) - 2
        # Calculate the average salary and return it with 5 decimal places
        return round(sum_salary / count, 5)
