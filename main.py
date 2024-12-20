import pandas as pd
import sys
sys.path.append('src')
from sqlalchemy import create_engine
from src.deviation_calculation import calculate_least_squares
from src.verification import verify_function, plot_selected_functions
from src.mapping_data import calculate_max_deviation


train_data = pd.read_csv('data/train.csv');
ideal_data = pd.read_csv('data/ideal.csv');
test_data = pd.read_csv('data/test.csv');

#printing first few rows of datasets files
#print("Training file",train_data.head());
#print("Ideal file",ideal_data.head());
#print("Test file",test_data.head());

#creating sqlite engine
engine = create_engine('sqlite:///stock_database.db');

#loading the training data into the database
train_data.to_sql('training_data', engine,if_exists='replace',index=False);
#print("Training data loaded into the database");

ideal_data.to_sql('ideal_data_func',engine,if_exists='replace',index=False);
#print("Ideal data functions are loaded into the database");

test_data.to_sql('test_data',engine,if_exists='replace',index=False);
#print("Test data are loaded into the database");

#Load Training and Ideal Data
train_data = pd.read_sql('SELECT * FROM training_data',engine)
ideal_data = pd.read_sql('SELECT * FROM ideal_data_func', engine)

#Select best ideal functions
selected_functions = calculate_least_squares(train_data,ideal_data)
print("Selected Ideal functions:",selected_functions)

#Verify and plot
verify_function(train_data, ideal_data, selected_functions)
plot_selected_functions(train_data, ideal_data, selected_functions)

calculate_max_deviation(train_data,ideal_data,selected_functions)


