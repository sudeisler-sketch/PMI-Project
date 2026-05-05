import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv("pmi_weekly_project_data.csv")

features = ["SP500_return", "PM_volume"]
target = "PM_return"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

linear_predictions = linear_model.predict(X_test)

linear_mse = mean_squared_error(y_test, linear_predictions)
linear_r2 = r2_score(y_test, linear_predictions)

print("Linear Regression Results")
print("Mean Squared Error:", linear_mse)
print("R-squared:", linear_r2)


rf_model = RandomForestRegressor(random_state=42, n_estimators=20)
rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

rf_mse = mean_squared_error(y_test, rf_predictions)
rf_r2 = r2_score(y_test, rf_predictions)

print("\nRandom Forest Regressor Results")
print("Mean Squared Error:", rf_mse)
print("R-squared:", rf_r2)


plt.figure(figsize=(8, 5))
plt.scatter(y_test, rf_predictions)
plt.xlabel("Actual PM Weekly Return")
plt.ylabel("Predicted PM Weekly Return")
plt.title("Actual vs Predicted PM Weekly Returns - Random Forest")
plt.tight_layout()
plt.show()


feature_importance = pd.DataFrame({
    "Feature": features,
    "Importance": rf_model.feature_importances_
})

print("\nFeature Importance:")
print(feature_importance)
