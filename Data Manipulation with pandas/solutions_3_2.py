# Solutions for the job market and salaries exercises

# 1. Load the CSV file into a DataFrame
df = pd.read_csv('job_market_salaries.csv')

# 2. Calculate the average salary for each Experience_Level
average_salary_by_experience = {'Junior': 89166.66666666667, 'Mid': 110000.0, 'Senior': 137857.14285714287}

# 3. Find the company that offers the highest salary
highest_salary_company = {'Company': 'Google', 'Salary': 150000}

# 4. Count the number of job postings in each Industry
job_postings_by_industry = {'Tech': 11, 'Design': 2, 'Finance': 2, 'E-Commerce': 1, 'Automotive': 1, 'Media': 1, 'HR': 1, 'Sales': 1}

# 5. Identify the most common Job_Title in the dataset
most_common_job = 'Data Scientist'

# 6. Filter and display only the jobs in the Tech industry
tech_industry_jobs = df[df['Industry'] == 'Tech']

# 7. Create a pivot table showing the average salary by Location and Experience_Level
salary_pivot = {'Junior': {'Austin': 95000.0, 'Boston': nan, 'Chicago': nan, 'Dallas': nan, 'Denver': 80000.0, 'Houston': nan, 'Los Angeles': nan, 'Miami': 95000.0, 'New York': nan, 'San Diego': 90000.0, 'San Francisco': 85000.0, 'Seattle': 90000.0}, 'Mid': {'Austin': nan, 'Boston': 107500.0, 'Chicago': 115000.0, 'Dallas': nan, 'Denver': nan, 'Houston': nan, 'Los Angeles': 110000.0, 'Miami': nan, 'New York': 100000.0, 'San Diego': 110000.0, 'San Francisco': 120000.0, 'Seattle': nan}, 'Senior': {'Austin': 130000.0, 'Boston': nan, 'Chicago': 140000.0, 'Dallas': 145000.0, 'Denver': nan, 'Houston': 140000.0, 'Los Angeles': nan, 'Miami': 125000.0, 'New York': 150000.0, 'San Diego': nan, 'San Francisco': nan, 'Seattle': 135000.0}}

# 8. Group by Company and calculate the total number of job postings and the average salary they offer
company_group = {'total_postings': {'Adobe': 1, 'Airbnb': 1, 'Amazon': 1, 'Apple': 1, 'Cisco': 1, 'Facebook': 1, 'Google': 1, 'IBM': 1, 'Intel': 1, 'LinkedIn': 1, 'Microsoft': 1, 'Netflix': 1, 'Oracle': 1, 'Paypal': 1, 'Salesforce': 1, 'Snapchat': 1, 'Spotify': 1, 'Tesla': 1, 'Twitter': 1, 'Uber': 1}, 'average_salary': {'Adobe': 80000.0, 'Airbnb': 95000.0, 'Amazon': 90000.0, 'Apple': 145000.0, 'Cisco': 110000.0, 'Facebook': 110000.0, 'Google': 150000.0, 'IBM': 140000.0, 'Intel': 125000.0, 'LinkedIn': 110000.0, 'Microsoft': 120000.0, 'Netflix': 115000.0, 'Oracle': 140000.0, 'Paypal': 90000.0, 'Salesforce': 85000.0, 'Snapchat': 100000.0, 'Spotify': 105000.0, 'Tesla': 130000.0, 'Twitter': 135000.0, 'Uber': 95000.0}}

# 9. Find the job that was posted most recently
most_recent_job = {'Job_Title': 'Data Engineer', 'Company': 'Intel', 'Location': 'Miami', 'Experience_Level': 'Senior', 'Salary': 125000, 'Industry': 'Tech', 'Date_Posted': Timestamp('2024-10-05 00:00:00')}

# 10. Create a cumulative sum of salaries and display it
df['Cumulative_Salary'] = [150000, 270000, 360000, 470000, 600000, 715000, 855000, 935000, 1040000, 1135000, 1280000, 1390000, 1475000, 1575000, 1710000, 1805000, 1945000, 2055000, 2145000, 2270000]
