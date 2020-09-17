import pandas as pd
import matplotlib.pyplot as plt

def get_response_chance(data_subset):
    '''
        Returns the proportion of responses that are "Yes" for the data_subset given.
        Returns 0 if the data_subset is empty.
    '''
    
    positive = data_subset[data_subset['Response'] == "Yes"]
    try:
        return len(positive)/len(data_subset)
    except:
        return 0
    
def get_response_continuous(data, column, bin_count = 20, axis = None):
    '''
        Given a dataframe and a column name, plots the response chance for each bin, which by default spans 1/20 of the range.
        axis should be specified for subplots, or None if subplots are not being used.
        This method should only be used on columns with continuous data.
    '''

    column_min, column_max = min(data[column]), max(data[column])

    step = int((column_max - column_min) / bin_count)
    bins = range(int(column_min), int(column_max - step), step)
    response_chart = []
    
    # iterate through each bin, calculation the response_chance for the data entries in that bin
    for i in bins:
        temp_min, temp_max = i, i + step
        column_subset = data[data[column] >= temp_min]
        column_subset = column_subset[column_subset[column] < temp_max]
        response_chart.append((i, get_response_chance(column_subset)))
    
    # graph data
    dataFrame = pd.DataFrame(data=response_chart, columns=[column, 'Response chance'])
    
    if axis == None:
        dataFrame.plot.line(x = column, y = 'Response chance', title = 'Response Chance Based on ' + column)
    else:
        dataFrame.plot.line(x = column, y = 'Response chance', title = 'Response Chance Based on ' + column, ax = axis)
    
def get_response_categorical(data, column, axis = None):
    '''
        Given a dataframe and a column name, plots the response chance for each possible category.
        axis should be specified for subplots, or None if subplots are not being used.
        This method should only be used on columns with categorical data.
    '''
    
    bins = data[column].unique()
    response_chart = []
    
    # iterate through each category, calculation the response_chance for the data entries in that category
    for i in bins:
        column_subset = data[data[column] == i]
        response_chart.append((i, get_response_chance(column_subset)))
    
    # graph data
    dataFrame = pd.DataFrame(data=response_chart, columns=[column, 'Response chance'])
    
    if axis == None:
        dataFrame.sort_values(column).plot.bar(x = column, y = 'Response chance', title = 'Response Chance Based on ' + column)
    else:
        dataFrame.sort_values(column).plot.bar(x = column, y = 'Response chance', title = 'Response Chance Based on ' + column, ax = axis)