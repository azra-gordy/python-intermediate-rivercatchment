"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views


def analyse_data(data_dir):
    """Calculate the standard deviation by day between datasets.

    Gets all the measurement data from the CSV files in the data directory,
    works out the mean for each day, and then graphs the standard deviation
    of these means.
    """
    #data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
    #if len(data_file_paths) == 0:
    data_file_paths = load_catchment_data(data_dir)    
    data = map(models.read_variable_from_csv, data_file_paths)
    daily_standard_deviation = compute_standard_deviation_by_day(data)
    return daily_standard_deviation

def load_catchment_data(data_dir):
    data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError('No CSV files found in the data directory')
    return data_file_paths

def compute_standard_deviation_by_day(data):
    #daily_std_list = []
    daily_std_list = map(models.daily_std, data)
    #for dataset in data:
    #    daily_std = dataset.groupby(dataset.index.date).std()
    #    daily_std_list.append(daily_std)
    return  pd.concat(daily_std_list)
    
