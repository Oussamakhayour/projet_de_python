import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Génération de variables aléatoires (rvs)
random_samples = norm.rvs(size=1000)

# Tracer de la fonction de densité de probabilité (pdf)
x = np.linspace(-3, 3, 100)
pdf_values = norm.pdf(x)
plt.plot(x, pdf_values, label='PDF')