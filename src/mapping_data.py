import math

#creating function to calculate max deviation for training data
def calculate_max_deviation(train_data,ideal_data,selected_function):
    max_deviations={}
    for train_col,ideal_col in selected_function.items():
        deviations = abs(train_data[train_col] - ideal_data[ideal_col])
        #print("Train data",train_data[train_col])
        #print("Ideal data",ideal_data[ideal_col])
        #print("Absolute value",abs(train_data[train_col] - ideal_data[ideal_col]))
        max_deviations[train_col] = deviations.max()
    return max_deviations

#function too map this max_deviation to ideal functions
def map_test_data(test_data, ideal_data,selected_functions,max_deviations):
    mapped_data = []
    for index, row in test_data.iterrows():
        x_test, y_test = row['x'],row['y']
        for train_col,ideal_col in selected_functions.items():
            ideal_y = ideal_data.loc[ideal_data['x'] == x_test,ideal_col].values
            if ideal_y.size > 0:
                deviation = abs(y_test - ideal_y[0])
                if deviation <= max_deviations[train_col]*math.sqrt(2):
                    mapped_data.append({
                        'x': x_test,
                        'y': y_test,
                        
                    })
