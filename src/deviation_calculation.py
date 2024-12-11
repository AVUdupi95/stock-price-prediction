import numpy as np

def calculate_least_squares(train_data,ideal_data,col_count = 4):

    """
    Calculate the least squares deviation and select the best ideal functions.
    """

    selected_func = {};

    for i in range(1, col_count + 1):
        min_deviation = float('inf')
        best_fit = None

        train_col = f'y{i}'
        for j in range(1, ideal_data.shape[1]):
            ideal_col = f'y{j}'
            deviation = np.sum((train_data[train_col] - ideal_data[ideal_col])**2)

            if deviation < min_deviation:
                min_deviation = deviation
                best_fit = ideal_col

        selected_func[train_col] = best_fit
    return selected_func


