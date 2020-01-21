import numpy as np
from bokeh.plotting import figure, show, output_file

#Function for converting dates to the proper format
def datetime(x):
    return np.array(x, dtype = np.datetime64)

def plot(ip):
    ip = ip.rstrip('\n')
    #Creating a new plot with various optional parameters
    p = figure(x_axis_type = "datetime", title = "{} Ping Response".format(ip))

    #Extracting data from .txt file
    cpu_data = open ('Your-Path\\{}.txt'.format(ip)).readlines()
    values = []
    for each in cpu_data:
        if each.split(',')[0] == 'np.nan':
            values.append(each.split(',')[0])

        else:
            values.append(float(each.split(',')[0]))

    dates = []
    for each in cpu_data:
        dates.append((each.split(',')[1]).rstrip('\n'))

    #Converting dates to the proper format and drawing the lines
    p.line(datetime(dates), values, color = 'blue', legend = 'Ping_Response')

    #Setting the location of the legend on the plot
    p.legend.location = "top_left"
 
    #Creating the output HTML file in the current folder
    output_file("{}_ping_response.html".format(ip), title = "{} Ping Response".format(ip))
 
    #Displaying the final result
    show(p)
    print(ip)