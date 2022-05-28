import statistics
import pandas as pd
import random

import plotly.figure_factory as ff

df = pd.read_csv ("medium_data.csv")

data = df["reading_time"].tolist()

fig=ff.create_distplot ( [data], ["reading_time"], show_hist= False)

fig.show()

population_mean=statistics.mean(data)

print("Mean = ", population_mean)

population_standarddeviation = statistics.stdev(data) 
print("Standard Deviation = ", population_standarddeviation)


def random_set_of_mean(counter): 
    dataset = [] 
    for i in range(0, counter):
        random_index= random.randint(0, len (data)) 
        value = data[random_index] 
        dataset.append(value)
    mean = statistics.mean(dataset) 


def setup():
  mean_list = []
  for i in range(0,100):
        set_of_means= random_set_of_mean (30)
        mean_list.append(set_of_means)
  fig.show(mean_list)


def show_fig(mean_list): 
    df =  mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist=False) 
    fig.show()  
