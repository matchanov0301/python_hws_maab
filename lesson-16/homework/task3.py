import pandas as pd

iris_df = pd.read_json("iris.json")
iris_df.columns = [col.lower() for col in iris_df.columns]
numerical_stats = iris_df[['sepallength', 'sepalwidth', 'petallength', 'petalwidth']].agg(['mean', 'median', 'std'])
print(numerical_stats, "\n")

titanic_df = pd.read_excel("titanic.xlsx")
age_stats = {
    "min_age": titanic_df["Age"].min(),
    "max_age": titanic_df["Age"].max(),
    "sum_age": titanic_df["Age"].sum()
}
print(age_stats, "\n")

movie_df = pd.read_csv("movie.csv")
director_likes = movie_df.groupby("director_name")["director_facebook_likes"].sum()
top_director = director_likes.idxmax()
top_director_likes = director_likes.max()
print(f"Director: {top_director}, Total Likes: {top_director_likes}\n")

longest_movies = movie_df[["director_name", "duration"]].nlargest(5, "duration")
print(longest_movies, "\n")

flights_df = pd.read_parquet("flights.parquet")
missing_values = flights_df.isnull().sum()
print("Missing values:\n", missing_values)

flights_df.fillna(flights_df.mean(), inplace=True)
