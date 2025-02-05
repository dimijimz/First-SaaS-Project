# train_model.py
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Dummy data:
# Let's assume our features are:
# - temperature (°F)
# - humidity (%)
# - day_of_week (1 for Monday, 7 for Sunday)
# - local_event (1 if an event is happening, else 0)
#
# For example, X is an array with rows representing different days:
X = np.array([
    [70, 50, 1, 0],
    [75, 55, 2, 1],
    [80, 60, 3, 0],
    [65, 45, 4, 0],
    [85, 65, 5, 1]
])

# Dummy target variable (e.g., predicted demand)
# These values are made up for demonstration purposes.
y = np.array([100, 120, 150, 80, 160])

# Create and train a simple linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the trained model to a file named demand_model.pkl
with open('demand_model.pkl', 'wb') as f:
    pickle.dump(model, f)
    
# Placeholder test to show dummy model working
print("Dummy demand forecasting model trained and saved as demand_model.pkl")
