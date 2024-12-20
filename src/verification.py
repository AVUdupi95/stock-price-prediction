import matplotlib.pyplot as plot
import numpy as np

#recalculate and display deviations for selected functions
def verify_function(train_data,idela_data,sel_func):
    for train_col,ideal_col in sel_func.items():
        deviation = np.sum((train_data[train_col] - idela_data[ideal_col])**2)
        print(f"Deviation for {train_col} vs {ideal_col}: {deviation}")

#Plot training and ideal functions
def plot_selected_functions(train_data, ideal_data, selected_functions):
    for train_column, ideal_column in selected_functions.items():
        plot.figure(figsize=(10, 5))
        plot.plot(train_data['x'], train_data[train_column], label=f"Training: {train_column}", marker='o')
        plot.plot(ideal_data['x'], ideal_data[ideal_column], label=f"Ideal: {ideal_column}", linestyle='--')
        plot.title(f"Comparison of {train_column} and {ideal_column}")
        plot.xlabel('x')
        plot.ylabel('y')
        plot.legend()
        plot.grid(True)
        #plot.show()


