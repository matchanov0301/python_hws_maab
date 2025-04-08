import pandas as pd


movie_df = pd.read_csv('movie.csv')


df_color = movie_df[['director_name', 'color']]
df_reviews = movie_df[['director_name', 'num_critic_for_reviews']]


left_join = pd.merge(df_color, df_reviews, on='director_name', how='left')


outer_join = pd.merge(df_color, df_reviews, on='director_name', how='outer')


print(f"Left Join Rows: {len(left_join)}")
print(f"Outer Join Rows: {len(outer_join)}")
