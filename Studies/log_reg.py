import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data: hours studied vs. exam result (pass or fail)
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Reshape for single feature
exam_result = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # 0 = fail, 1 = pass

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(hours_studied, exam_result, test_size=0.2, random_state=42)

# Create and train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Plot decision boundary (optional)
plt.figure(figsize=(8, 6))
plt.scatter(X_train, y_train, color='blue', label='Training Data')
plt.scatter(X_test, y_test, color='green', label='Testing Data')
plt.plot(hours_studied, model.predict_proba(hours_studied)[:, 1], color='red', label='Decision Boundary')
plt.xlabel('Hours Studied')
plt.ylabel('Probability of Passing Exam')
plt.title('Logistic Regression')
plt.legend()
plt.grid(True)
plt.show()
