import pandas as pd

titanic_df = pd.read_excel('titanic.xlsx')

def classify_age(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'

titanic_df['Age_Group'] = titanic_df['Age'].apply(classify_age)


print("Titanic with Age Group classification:")
print(titanic_df[['Age', 'Age_Group']].head())
