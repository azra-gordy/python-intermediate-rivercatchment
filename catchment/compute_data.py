"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views


def daily_std(dataset):
    return dataset.groupby(dataset.index.date).std()

def map_compute_standard_deviation_by_day(data):
    #daily_std_list = map(daily_std, data)
    return pd.concat(map(daily_std, data))

def compute_standard_deviation_by_day(data):
    daily_std_list = []
    for dataset in data:
        daily_std = dataset.groupby(dataset.index.date).std()
        daily_std_list.append(daily_std)
    
    return pd.concat(daily_std_list)

def load_catchment_data(data_dir):
    data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError('No CSV files found in the data directory')
    return map(models.read_variable_from_csv, data_file_paths) 

def analyse_data(data_dir):
    """Calculate the standard deviation by day between datasets.

    Gets all the measurement data from the CSV files in the data directory,
    works out the mean for each day, and then graphs the standard deviation
    of these means.
    """
    return  map_compute_standard_deviation_by_day(load_catchment_data(data_dir))

    #graph_data = {
    #    'daily standard deviation': daily_standard_deviation
    #}

    #views.visualize(graph_data)
