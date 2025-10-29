from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X_train, y_train)

tree_rules = export_text(model, feature_names=data.feature_names)
print("Decision Tree Structure:\n")
print(tree_rules)


y_pred = model.predict(X_test)
print("\nPredictions:", y_pred)
print("Actual:", y_test)
print("\nAccuracy:", accuracy_score(y_test, y_pred))

new_sample = [[5.1, 3.5, 1.4, 0.2]]  # Example input
prediction = model.predict(new_sample)
print("\nNew Sample Prediction:", data.target_names[prediction][0])
