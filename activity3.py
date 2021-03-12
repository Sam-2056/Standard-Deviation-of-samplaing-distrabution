import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

def random_set_mean (counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = [] 
    for x in range(0, 1000):
        set_of_mean = random_set_mean (100)
        mean_list.append(set_of_mean)
    show_fig(mean)

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)

    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

    print("Mean of sample: ",mean)

setup()

def stand_dev():
    mean_list = [] 
    for x in range(0, 1000):
        set_of_mean = random_set_mean (100)
        mean_list.append(set_of_mean)
    std_dev = statistics.stdev(mean_list)

    print("Standard Deviation of samplaing distrabution: ", std_dev)

stand_dev()