"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views


def analyse_data(dataset):
    """works out the mean for each day, and then graphs the standard deviation
    of these means.
    """
    #= CSVDataSource(data_dir)
    data = dataset.load_catchment_data() 

    #data = CSV_data.load_catchment_data() 
    daily_standard_deviation = compute_standard_deviation_by_day(data)
    return daily_standard_deviation

class CSVDataSource:
    def __init__(self,data_dir):
        self.data_dir = data_dir
        
    def load_catchment_data(self):
        """"Gets all the measurement data from the CSV files in the data directory"""
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError('No CSV files found in the data directory')
        data = map(models.read_variable_from_csv, data_file_paths)
        return data

class JSONDataSource:
    def __init__(self,data_dir):
        self.data_dir = data_dir
        
    def load_catchment_data(self):
        """"Gets all the measurement data from the CSV files in the data directory"""
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.json'))
        if len(data_file_paths) == 0:
            raise ValueError('No JSON files found in the data directory')
        data = map(models.read_variable_from_json, data_file_paths)
        return data

#read_variable_from_json

def compute_standard_deviation_by_day(data):
    """Calculate the standard deviation by day between datasets"""
    daily_std_list = map(models.daily_std, data)
    return  pd.concat(daily_std_list)
    
