import pandas as pd
import sqlite3


conn = sqlite3.connect("chinook.db")


customers_df = pd.read_sql_query("SELECT * FROM customers", conn)


print("=== Chinook Customers (First 10 Rows) ===")
print(customers_df.head(10))
print("\n")


iris_df = pd.read_json("iris.json")


print("=== Iris Dataset ===")
print("Shape:", iris_df.shape)
print("Columns:", iris_df.columns.tolist())
print("\n")


titanic_df = pd.read_excel("titanic.xlsx")

print("=== Titanic Dataset (First 5 Rows) ===")
print(titanic_df.head())
print("\n")


flights_df = pd.read_parquet("flights.parquet")

print("=== Flights Dataset Summary ===")
flights_df.info()
print("\n")

movie_df = pd.read_csv("movie.csv")


print("=== Movie Dataset (Random 10 Rows) ===")
print(movie_df.sample(10))
print("\n")
