# Use normal case switch to create option menu and look up tips to make it look more professional
#Find ways to neatly represent data 

import matplotlib.pyplot as plt
import pandas as pd
import os



def temperature():
    all_data = pd.read_csv("data.csv")
    #Orders data by date, so pm25 value for 1/1/23 comes first
    #pm25 value after grouping if printed shows everything in date order
    ordered = all_data.groupby("time").sum(numeric_only=True)
    temp = ordered['temperature']

    #graph for temperature
    temp.plot(title = "A graph to show the change in temperature over our recordered  data", color='red')
    plt.xlabel("Time in seconds")
    plt.ylabel("Temperature in celsius")
    plt.legend(loc='upper center')
    plt.show()


def humidity():
    all_data = pd.read_csv("data.csv")
    #Orders data by date, so pm25 value for 1/1/23 comes first
    #pm25 value after grouping if printed shows everything in date order
    ordered = all_data.groupby("time").sum(numeric_only=True)
    humidity = ordered['humidity']

    #graph for temperature
    humidity.plot(title = "A graph to show the change in humidity over our recorded data", color='pink')
    plt.xlabel("Time in seconds")
    plt.ylabel("Humidity %")
    plt.legend(loc='upper center')
    plt.show()

def eco2():
    all_data = pd.read_csv("data.csv")
    #Orders data by date, so pm25 value for 1/1/23 comes first
    #pm25 value after grouping if printed shows everything in date order
    ordered = all_data.groupby("time").sum(numeric_only=True)
    eco2 = ordered['eCO2Value']

    #graph for temperature
    eco2.plot(title = "A graph to show the change in CO2 levels over our recorded data", color='green')
    plt.xlabel("Time in seconds")
    plt.ylabel("eCO2 ppm")
    plt.legend(loc='upper left')
    plt.show()

def iaqscore():
    all_data = pd.read_csv("data.csv")
    #Orders data by date, so pm25 value for 1/1/23 comes first
    #pm25 value after grouping if printed shows everything in date order
    ordered = all_data.groupby("time").sum(numeric_only=True)
    iaqScore = ordered['iaqScore']

    #graph for temperature
    iaqScore.plot(title = "Graph to show the recorded indoor air quality", color='green')
    plt.xlabel("Time in seconds")
    plt.ylabel("A score from 0 - 150")
    plt.legend(loc='upper left')
    plt.show()

def iaqpercent():
    all_data = pd.read_csv("data.csv")
    #Orders data by date, so pm25 value for 1/1/23 comes first
    #pm25 value after grouping if printed shows everything in date order
    ordered = all_data.groupby("time").sum(numeric_only=True)
    iaqPercent = ordered['iaqPercent']

    #graph for temperature
    iaqPercent.plot(title = "Graph to show the recorded indoor air quality percentage", color='green')
    plt.xlabel("Time in seconds")
    plt.ylabel("IAQ %")
    plt.legend(loc='upper center')
    plt.show()


i=0
while i == 0:

    print("1. Temperature")
    print("2. Humidity")
    print("3. eCO2")
    print("4. IAQ Score")
    print("5. IAQ Percent")
    option = input("Please select the data type you wish to see: ").lower()

    match option:
        case "temperature" | "1":
            temperature()
            i=0

            
    
        case "humidity" | "2":
            humidity()
            i=0
            

        case "eco2" | "3":
            eco2()
            i=0
            
        case "iaq score" | "4":
            iaqscore()
            i=0

        case "iaq percent" | "5":
            iaqpercent()
            i=0

        case _:
            print("Please ensure a number between 1 -5 or a data type listed above has been entered.")
            i=10



            










