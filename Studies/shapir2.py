from scipy.stats import shapiro

# Sample data (replace with your data)
data = [0.1, 0.5, 0.7, 1.2, 0.8, 0.6, 1.1, 0.9, 1.0, 0.3]

# Perform Shapiro-Wilk test
statistic, p_value = shapiro(data)

# Print test statistic and p-value
print("Test Statistic:", statistic)
print("p-value:", p_value)

# Interpret the result
if p_value > 0.05:
    print("Sample looks Gaussian (fail to reject H0)")
else:
    print("Sample does not look Gaussian (reject H0)")
