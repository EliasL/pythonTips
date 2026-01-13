import pandas as pd

df = pd.read_csv("example.csv")

experiment_data = df[df["time"] >= 0]

print(experiment_data["energy"].iloc[0])
# print(experiment_data["energy"][0])
# 12.1
# KeyError: 0


print(df["time"])
# [-2, -1, 0, 1]

print(df["time"] >= 0)
# [False, False, True, True]

print(df[[False, False, True, True]])
#    nr  energy  time
# 2  3    12.1     0
# 3  4    23.0     1
