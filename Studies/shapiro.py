import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate sample data from a normal distribution
np.random.seed(0)
sample_data = np.random.normal(loc=0, scale=1, size=1000)

# Generate theoretical quantiles for a normal distribution
theoretical_quantiles = np.random.normal(loc=0, scale=1, size=1000)

# Sort sample data and theoretical quantiles
sample_data_sorted = np.sort(sample_data)
theoretical_quantiles_sorted = np.sort(theoretical_quantiles)

# Create Q-Q plot
plt.figure(figsize=(6, 6))
plt.scatter(theoretical_quantiles_sorted, sample_data_sorted, color='blue', alpha=0.5)
plt.plot([-3, 3], [-3, 3], color='red', linestyle='--')  # Plot diagonal line for reference
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Data Quantiles')
plt.title('Q-Q Plot')
plt.grid(True)
plt.show()
