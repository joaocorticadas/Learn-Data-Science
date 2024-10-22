import pandas as pd
import numpy as np


#Exercise 1
jobs = pd.read_csv("job_market_salaries.csv")

print(jobs.head())

#Exercise 2
ave_salary_exper = jobs.groupby("Experience_Level")["Salary"].mean()
print(ave_salary_exper)

#Exercise 3
highest_salary = jobs.sort_values("Salary",  ascending=False)
print(highest_salary.loc[0, "Company"])


