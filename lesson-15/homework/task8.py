import matplotlib.pyplot as plt
import numpy as np

categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']


category_A = [10, 20, 15, 30]
category_B = [25, 30, 20, 15]
category_C = [30, 25, 35, 20]

# Stack the bars
plt.bar(time_periods, category_A, label='Category A', color='skyblue')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B', color='salmon')
plt.bar(time_periods, category_C, bottom=np.array(category_A) + np.array(category_B), label='Category C', color='lightgreen')

plt.title("Stacked Bar Chart: Contribution of Categories Over Time")
plt.xlabel("Time Periods")
plt.ylabel("Value")
plt.legend()

plt.show()
