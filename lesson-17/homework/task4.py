import pandas as pd

movie_df = pd.read_csv('movie.csv')

grouped_movie_df = movie_df.groupby(['color', 'director_name']).agg(
    Total_Reviews=('num_critic_for_reviews', 'sum'),
    Average_Duration=('duration', 'mean')
).reset_index()

print("Multi-level Grouping on Movie Data:")
print(grouped_movie_df)
