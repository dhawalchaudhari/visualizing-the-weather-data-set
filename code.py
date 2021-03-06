# --------------
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import datetime
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# Generate a line chart that visualizes the readings in the months

def line_chart(df,period,col):
    """ A line chart that visualizes the readings in the months
    
    This function accepts the dataframe df ,period(day/month/year) and col(feature), which plots the aggregated value of the feature based on the periods. Ensure the period labels are properly named.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    period - Period of time over which you want to aggregate the data
    col - Feature of the dataframe
    
    """
    plt.plot(period,df[col], color = 'blue')
    plt.ylabel(col)
    plt.xticks(rotation = 90)
    plt.show()
    

# Function to perform univariate analysis of categorical columns
def plot_categorical_columns(df):
    """ Univariate analysis of categorical columns
    
    This function accepts the dataframe df which analyzes all the variable in the data and performs the univariate analysis using bar plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    
    """
    cat_data_columns = df.columns
    ncol = len(cat_data_columns)
    for col in cat_data_columns:
        df[col].value_counts().plot(kind = 'bar')
        plt.xlabel(col)
        plt.show()
    

# Function to plot continous plots
def plot_cont(df,plt_typ):
    """ Univariate analysis of Numerical columns
    
    This function accepts the dataframe df, plt_type(boxplot/distplot) which analyzes all the variable in the data and performs the univariate analysis using boxplot or distplot plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    plt_type - type of plot through which you want to visualize the data
    
    """
    num_data_columns = df.columns
    # fig, axs = plt.subplots(len(num_data_columns)//2,2, figsize = (15,10))
    # fig, axs = plt.subplots(3,2, figsize = (15,10))

    for i,col in enumerate(num_data_columns):
        if plt_typ == 'distplot':
            sns.distplot(df[col])
            plt.xlabel(col)
            plt.show()
        if plt_typ == 'boxplot':
            sns.distplot(df[col])
            plt.xlabel(col)
            plt.show()

# Function to plot grouped values based on the feature
def group_values(df,col1,agg1,col2):
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 2 column(feature) and aggregated function(agg1) which groupby the dataframe based on the column and plots the bar plot.
   
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    col2 - Feature of the dataframe to be plot against grouped data.
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    aggregate = {'mean':np.mean,'max':np.max,'min':np.min,'sum':np.sum,'len':len}
    grouping = df.groupby(col1)[col2].agg(aggregate[agg1])
    plt.figure(figsize = (10, 4))
    plt.ylabel(col2)
    grouping.plot(kind = "bar")
    plt.show()
    
    




# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'
weather_df = pd.read_csv(path, parse_dates = True, index_col = 'Date/Time')

# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.
per_day = weather_df.groupby(weather_df.index.day).mean()
per_month = weather_df.groupby(weather_df.index.month).mean()
per_year = weather_df.groupby(weather_df.index.year).mean()
calendar_month = calendar.month_name[1:]
line_chart(per_month,calendar_month,'Temp (C)')


# Now let's perform the univariate analysis of categorical features.
# Call the "function plot_categorical_columns()" with appropriate parameters.
cat_data = weather_df.select_dtypes(include = 'object')
plot_categorical_columns(cat_data)

# Let's plot the Univariate analysis of Numerical columns.
# Call the function "plot_cont()" with the appropriate parameters to plot distplot
num_data = weather_df.select_dtypes(include='number')
plot_cont(num_data,'distplot')

# Call the function "plot_cont()" with the appropriate parameters to plot boxplot
plot_cont(num_data,'boxplot')

# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.
# Feel free to try on diffrent features and aggregated functions like max, min.
group_values(weather_df, 'Weather', 'mean', 'Visibility (km)')



