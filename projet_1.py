from numpy import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
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
#data = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
#data_1= np.array([[1, -2, 3],
#                 [-4, 5, -6],
#                 [7, -8, 9]])
#mean_val = np.mean(data)
# median_val = np.median(data)
#std_dev = np.std(data)
#total_sum = np.sum(data)
#Corrélation = np.corrcoef(data, data_1)
#Covariance = np.cov(data, data_1)


#print("Moyenne:", mean_val)
#print("Médiane:", median_val)
#print("Écart-type:", std_dev)
#print("Somme totale:", total_sum)
#print("Corrélation:\n",Corrélation)
#print("Covariance:\n",Covariance)
# Générer des échantillons à partir d'une distribution normale
mean = 0
std_dev = 1
sample_size = 1000
data = np.random.normal(mean, std_dev, sample_size)

# Calculer la moyenne et l'écart-type des échantillons
sample_mean = np.mean(data)
sample_std_dev = np.std(data)

# Afficher des informations sur les échantillons générés
print(f"Moyenne de l'échantillon : {sample_mean}")
print(f"Écart-type de l'échantillon : {sample_std_dev}")

# Tracer l'histogramme des échantillons
plt.hist(data, bins=30, density=True, alpha=0.5, color='b')

# Tracer la distribution normale théorique pour comparaison
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)
plt.plot(x, p, 'k', linewidth=2)

# Ajouter des annotations au graphique
title = "Fit results: mean = %.2f,  std = %.2f" % (sample_mean, sample_std_dev)
plt.title(title)
plt.show()