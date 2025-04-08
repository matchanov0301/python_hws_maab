import pandas as pd


employee_df = pd.read_csv('employee.csv')


employee_df['Normalized_Salary'] = employee_df.groupby('DEPARTMENT')['BASE_SALARY'].transform(
    lambda x: (x - x.mean()) / x.std()
)


print(employee_df[['UNIQUE_ID', 'POSITION_TITLE', 'DEPARTMENT', 'BASE_SALARY', 'Normalized_Salary']].head())
