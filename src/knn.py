import ast

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import KFold

# Test different values of k
K_VALUES = [1, 3, 5, 7, 10, 15, 20, 30, 40, 50]

MODEL = 'paraphrase-mpnet-base-v2'

class KNN:
    def __init__(self, filename):
        self.filename = filename
        pass

    def predict(X_train, y_train, X_val, k):
        similarity_matrix = cosine_similarity(X_val, X_train)
        predictions = []
        for idx, sim_scores in enumerate(similarity_matrix):
            similar_indices = np.argsort(sim_scores)[::-1][:k]
            similar_ratings = y_train[similar_indices]
            similar_scores = sim_scores[similar_indices]
            weighted_average = np.dot(similar_ratings, similar_scores) / similar_scores.sum()
            predictions.append(weighted_average)
        return np.array(predictions)
    
    def k_fold_cross_validation(self, k):
        # Perform k-fold cross-validation for each k
        for k in K_VALUES:
            fold_errors = []
            for train_index, val_index in kf.split(X):
                X_train, X_val = X[train_index], X[val_index]
                y_train, y_val = y[train_index], y[val_index]
                
                y_pred = knn_predict(X_train, y_train, X_val, k)
                fold_error = mean_squared_error(y_val, y_pred)
                fold_errors.append(fold_error)
            
            average_error = np.mean(fold_errors)
            average_errors.append(average_error)
            print(f"k={k}, Average MSE={average_error}")
