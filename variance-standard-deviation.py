import pandas as pd
import math

data = pd.read_csv(r"./data.csv", names=[0])
data = data.dropna()
data_len = len(data)
print(data)

total = 0
total_variance = 0
for i in range(data_len):
    globals()["x" + str(i)] = data.iloc[i][0]
    total += globals()["x" + str(i)]

mean = total / data_len
print("mean = " + str(mean))
for i in range(data_len):
    total_variance += (globals()["x" + str(i)] - mean) ** 2
population_variance = total_variance / data_len
population_variance_standard_deviation = math.sqrt(population_variance)
sample_variance = total_variance / (data_len - 1)
standard_deviation = math.sqrt(sample_variance)
print("Population variance = " + str(population_variance))
print("Population standard deviation = " + str(population_variance_standard_deviation))
print("Sample variance = " + str(sample_variance))
print("Sample standard deviation = " + str(standard_deviation))
input("Press Enter to continue...")
