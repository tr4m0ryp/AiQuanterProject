from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def train_model(data: pd.DataFrame):
    """
    Train a Random Forest model to predict meme success.
    """
    # Prepare features and target
    X = data[['sentiment_score', 'likes', 'comments', 'shares']]  # Features
    y = data['success']  # Target: 1 = success, 0 = failure
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    logging.info(f"Model Accuracy: {accuracy * 100:.2f}%")
    
    return model

def predict_meme_success(model, meme_data):
    """
    Predict the success of a meme based on the trained model.
    """
    features = np.array([meme_data['sentiment_score'], meme_data['likes'], meme_data['comments'], meme_data['shares']]).reshape(1, -1)
    prediction = model.predict(features)
    return 'Success' if prediction[0] == 1 else 'Failure'

# Example usage:
def example_usage():
    # Example training data (this should be replaced by actual data)
    data = pd.DataFrame({
        'sentiment_score': [0.8, 0.3, 0.7, 0.9, 0.2, 0.5],
        'likes': [1200, 30, 700, 1800, 20, 150],
        'comments': [200, 10, 50, 150, 5, 20],
        'shares': [100, 2, 30, 80, 1, 10],
        'success': [1, 0, 1, 1, 0, 0]  # 1 = success, 0 = failure
    })
    
    # Train the model
    model = train_model(data)
    
    # Example meme data for prediction
    new_meme = {'sentiment_score': 0.8, 'likes': 1000, 'comments': 150, 'shares': 60}
    
    # Predict success of the meme
    result = predict_meme_success(model, new_meme)
    print(f"Meme success prediction: {result}")

if __name__ == "__main__":
    example_usage()
