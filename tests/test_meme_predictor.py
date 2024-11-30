import unittest
from src.meme_predictor import train_model, predict_meme_success
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

class TestMemePredictor(unittest.TestCase)

    def test_train_model(self)
        # Example data (replace with actual data)
        data = pd.DataFrame({
            'sentiment_score' [0.8, 0.3, 0.7, 0.9, 0.2, 0.5],
            'likes' [1200, 30, 700, 1800, 20, 150],
            'comments' [200, 10, 50, 150, 5, 20],
            'shares' [100, 2, 30, 80, 1, 10],
            'success' [1, 0, 1, 1, 0, 0]  # 1 = success, 0 = failure
        })
        
        # Train the model
        model = train_model(data)
        
        # Check if model is a RandomForestClassifier
        self.assertIsInstance(model, RandomForestClassifier)
        
    def test_predict_meme_success(self)
        # Example data for prediction
        model = RandomForestClassifier()  # Use a pre-trained model
        model.fit([[0.8, 1200, 200, 100], [0.2, 30, 10, 2]], [1, 0])  # Dummy fit for testing
        meme_data = {'sentiment_score' 0.8, 'likes' 1000, 'comments' 150, 'shares' 60}
        
        # Predict meme success
        result = predict_meme_success(model, meme_data)
        
        # Check that the prediction is either 'Success' or 'Failure'
        self.assertIn(result, ['Success', 'Failure'])

if __name__ == __main__
    unittest.main()
