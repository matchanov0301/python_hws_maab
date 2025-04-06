import pandas as pd


iris_df = pd.read_json("iris.json")


iris_df.columns = [col.lower() for col in iris_df.columns]


sepal_df = iris_df[["sepallength", "sepalwidth"]]

print("=== Sepal Columns ===")
print(sepal_df.head())


titanic_df = pd.read_excel("titanic.xlsx")


age_above_30 = titanic_df[titanic_df["Age"] > 30]
print("=== Passengers older than 30 ===")
print(age_above_30.head(), "\n")

print("=== Gender Counts ===")
print(titanic_df["Sex"].value_counts(), "\n")



movie_df = pd.read_csv("movie.csv")


long_movies = movie_df[movie_df["duration"] > 120]


sorted_long_movies = long_movies.sort_values(
    by="director_facebook_likes", ascending=False
)

print("=== Long Movies Sorted by Director Facebook Likes ===")
print(sorted_long_movies[["director_name", "duration", "director_facebook_likes"]].head(), "\n")
