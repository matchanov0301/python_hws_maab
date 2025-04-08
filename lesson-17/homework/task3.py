import pandas as pd


titanic_df = pd.read_excel('titanic.xlsx')

grouped_df = titanic_df.groupby('Pclass').agg(
    Average_Age=('Age', 'mean'),
    Total_Fare=('Fare', 'sum'),
    Passenger_Count=('PassengerId', 'count')
).reset_index()

print("Grouped Aggregations on Titanic:")
print(grouped_df)
