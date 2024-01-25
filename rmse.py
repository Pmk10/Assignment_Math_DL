import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    
    # Calculate the squared differences
    squared_diff = (pred - tar) ** 2
    
    # Calculate the mean squared error
    mse = np.mean(squared_diff)
    
    # Calculate the square root to get the RMSE
    rmse_value = np.sqrt(mse)
    
    return rmse_value