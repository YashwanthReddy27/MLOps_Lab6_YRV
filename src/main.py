from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

if __name__ == '__main__':
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Load the Breast Cancer dataset (binary classification)
    breast_cancer = load_breast_cancer()
    X, y = breast_cancer.data, breast_cancer.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Define and train the Gradient Boosting Classifier
    model = GradientBoostingClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Model accuracy:", accuracy_score(y_test, y_pred))
    print("Model classification report:")
    print(classification_report(y_test, y_pred))

    # Save the trained model to the models directory
    joblib.dump(model, 'models/breast_cancer_model.pkl')

    print("The model training and saving were successful.")
    print("Model saved to: models/breast_cancer_model.pkl")