import pandas as pd


movie_df = pd.read_csv('movie.csv')


def classify_duration(duration):
    if duration < 60:
        return 'Short'
    elif 60 <= duration <= 120:
        return 'Medium'
    else:
        return 'Long'


movie_df['Duration_Class'] = movie_df['duration'].apply(classify_duration)


print("Movies with Duration Classification:")
print(movie_df[['movie_title', 'duration', 'Duration_Class']].head())
