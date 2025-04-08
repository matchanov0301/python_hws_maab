import pandas as pd

flights_df = pd.read_parquet('flights.parquet')

flights_df['ArrDelay'] = pd.to_numeric(flights_df['ArrDelay'], errors='coerce')
flights_df['DepDelay'] = pd.to_numeric(flights_df['DepDelay'], errors='coerce')

grouped_flights_df = flights_df.groupby(['Year', 'Month']).agg(
    Total_Flights=('FlightDate', 'count'),
    Average_Arrival_Delay=('ArrDelay', 'mean'),
    Max_Departure_Delay=('DepDelay', 'max')
).reset_index()


print("Nested Grouping on Flights:")
print(grouped_flights_df)
