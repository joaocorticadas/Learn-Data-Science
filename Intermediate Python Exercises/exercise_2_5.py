import numpy as np
import matplotlib.pyplot as plt 

np.random.seed(123)

def launch_dice():
  dice = np.random.randint(1, 7)
  return dice

def run_100_times():
  results = [0]
  for x in range(100):
    roll = launch_dice()
    if roll == 1 or roll == 2:
      if results[-1] >= 1:
        results[-1] = results[-1] - 1
    elif roll == 3 or roll == 4 or roll == 5:
      results[-1] = results[-1] + 1
    elif roll == 6:
      new_roll = launch_dice()
      results[-1] = results[-1] + new_roll
  return results

hist_array = []

for x in range(10000):
  hist_array.append(run_100_times())

hist_array = np.array(hist_array)

plt.hist(hist_array, bins=100)
plt.savefig('exercise_2_5_chart.png')