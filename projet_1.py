from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# x = random.randint(100)
# x = random.rand()
# x = random.randint(100, size=(5))
# x = random.randint(100, size=(5, 5))
# x = random.rand(5)
# x = random.choice([3, 5, 7, 9])
# x = random.choice([3, 5, 7, 9], size=(3, 5))
# x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
# print(x)
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
data_1= np.array([[1, -2, 3],
                 [-4, 5, -6],
                 [7, -8, 9]])
mean_val = np.mean(data)
median_val = np.median(data)
std_dev = np.std(data)
total_sum = np.sum(data)
Corrélation = np.corrcoef(data, data_1)
Covariance = np.cov(data, data_1)


print("Moyenne:", mean_val)
print("Médiane:", median_val)
print("Écart-type:", std_dev)
print("Somme totale:", total_sum)
print("Corrélation:\n",Corrélation)
print("Covariance:\n",Covariance)
