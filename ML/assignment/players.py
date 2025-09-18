import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Step 1: Load dataset
df = pd.read_csv(r"D:\Vishnu\cc\ML\assignment\player_data.csv")

# Step 2: Select numeric features and target
X = df[["Matches_Played","Shots_On_Target","Assists"]]
y = df["Goals"]

# Step 3: Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predict and evaluate
y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Step 6: Predict goals for a sample player
sample = pd.DataFrame({"Matches_Played":[30], "Shots_On_Target":[60], "Assists":[10]})
predicted_goals = model.predict(sample)
print("Predicted Goals for sample player:", round(predicted_goals[0]))
