"""Module containing models representing catchment data.

The Model layer is responsible for the 'business logic' part of the software.

Catchment data is held in a Pandas dataframe (2D array) where each column 
contains data for a single measurement site, and each row represents a single 
measurement time across all sites.
"""

import pandas as pd
import numpy as np



def read_variable_from_csv(filename, measurements='Rainfall (mm)'):
    """Reads a named variable from a CSV file, and returns a
    pandas dataframe containing that variable. The CSV file must contain
    a column of dates, a column of site ID's, and (one or more) columns
    of data - only one of which will be read.

    :param filename: Filename of CSV to load
    :return: 2D array of given variable. Index will be dates,
             Columns will be the individual sites
    """
    dataset = pd.read_csv(filename, usecols=['Date', 'Site', measurements])

    dataset = dataset.rename({'Date': 'OldDate'}, axis='columns')
    dataset['Date'] = [
        pd.to_datetime(x, dayfirst=True, format='mixed') for x in dataset['OldDate']
        ]
    dataset = dataset.drop('OldDate', axis='columns')

    newdataset = pd.DataFrame(index=dataset['Date'].unique())

    for site in dataset['Site'].unique():
        newdataset[site] = dataset[dataset['Site'] == site].set_index('Date')[measurements]

    newdataset = newdataset.sort_index()

    return newdataset


def read_variable_from_json(filename):
    """Reads a named variable from a JSON file, and returns a
    pandas dataframe containing that variable. The JSON file must contain
    a column of dates, a column of site ID's, and (one or more) columns
    of data - only one of which will be read.

    :param filename: Filename of JSON to load
    :return: 2D array of given variable. Index will be dates,
             Columns will be the individual sites
    """
    dataset = pd.read_json(filename, convert_dates=False)
    dataset = dataset[['Date', 'Site', 'Rainfall (mm)']]

    dataset = dataset.rename({'Date':'OldDate'}, axis='columns')
    dataset['Date'] = [pd.to_datetime(x,dayfirst=True) for x in dataset['OldDate']]
    dataset = dataset.drop('OldDate', axis='columns')

    newdataset = pd.DataFrame(index=dataset['Date'].unique())

    for site in dataset['Site'].unique():
        newdataset[site] = dataset[dataset['Site'] == site].set_index('Date')["Rainfall (mm)"]

    newdataset = newdataset.sort_index()

    return newdataset


def read_variable_from_xml(filename):
    """Reads a named variable from a XML file, and returns a
    pandas dataframe containing that variable. The XML file must contain
    a column of dates, a column of site ID's, and (one or more) columns
    of data - only one of which will be read.

    :param filename: Filename of XML to load
    :return: 2D array of given variable. Index will be dates,
             Columns will be the individual sites
    """
    dataset = pd.read_xml(filename)

    dataset = dataset.rename({'Date':'OldDate', 'Site_Name': 'Site Name', 'Rainfall_mm': 'Rainfall (mm)'}, axis='columns')
    dataset['Date'] = [pd.to_datetime(x,dayfirst=True) for x in dataset['OldDate']]
    dataset = dataset.drop('OldDate', axis='columns')

    newdataset = pd.DataFrame(index=dataset['Date'].unique())

    for site in dataset['Site'].unique():
        newdataset[site] = dataset[dataset['Site'] == site].set_index('Date')["Rainfall (mm)"]

    newdataset = newdataset.sort_index()

    return newdataset


def daily_total(data):
    """Calculate the daily total of a 2D data array.

    :param data: A 2D Pandas data frame with measurement data.
    Index must be np.datetime64 compatible format. Columns are measurement sites.
    :returns: A 2D Pandas data frame with total values of the measurements for each day.
    """
    return data.groupby(data.index.date).sum()


def daily_mean(data):
    """Calculate the daily mean of a 2D data array.

    :param data: A 2D Pandas data frame with measurement data.
    Index must be np.datetime64 compatible format.
    :returns: A 2D Pandas data frame with mean values of the measurements for each day.
    """
    return data.groupby(data.index.date).mean()


def daily_max(data):
    """Calculate the daily maximum of a 2D data array.

    :param data: A 2D Pandas data frame with measurement data.
    Index must be np.datetime64 compatible format.
    :returns: A 2D PAndas data frame with maximum values of the measurements for each day.
    """
    return data.groupby(data.index.date).max()


def daily_min(data):
    """Calculate the daily minimum of a 2D data array.

    :param data: A 2D Pandas data frame with measurement data.
    Index must be np.datetime64 compatible format.
    :returns: A 2D Pandas data frame with minimum values of the measurements for each day.
    """
    return data.groupby(data.index.date).min()


def data_normalise(data):
    """Normalise any given 2D data array
    
    :param data: A 2D Pandas data frame with measurement data.
    :returns : A normalised 2D Pandas data frame with measurement data.
    """
    normal_max = np.array(np.max(data, axis=0))
    return data / normal_max[np.newaxis, :]
