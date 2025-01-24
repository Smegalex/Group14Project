# Use normal case switch to create option menu and look up tips to make it look more professional
#Find ways to neatly represent data 

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation
import os

def get_data_from_csv():


    csv_directory = os.path.dirname(os.path.realpath(__file__))
    csv_directory = csv_directory[0:len(csv_directory)-7]
    csv_directory = os.path.join(csv_directory,"computer","data")


    sensor140 = pd.read_csv(csv_directory+"\sensor140.csv")
    sensor141 = pd.read_csv(csv_directory+"\sensor141.csv")
    sensor142 = pd.read_csv(csv_directory+"\sensor142.csv")
    sensor143 = pd.read_csv(csv_directory+"\sensor143.csv")


    return sensor140,sensor141,sensor142,sensor143


def animate(i,variable_name,show_name,unit_name):
    sensor140, sensor141, sensor142, sensor143 = get_data_from_csv()
    
    # Order data by date for each sensor
    ordered140 = sensor140.groupby("time").sum(numeric_only=True)
    ordered141 = sensor141.groupby("time").sum(numeric_only=True)
    ordered142 = sensor142.groupby("time").sum(numeric_only=True)
    ordered143 = sensor143.groupby("time").sum(numeric_only=True)
    
    # Clear the previous plot
    plt.clf()
    
    # Plot temperature data for each sensor
    plt.plot(ordered140.index, ordered140[variable_name], label='Sensor 140', color='red')
    plt.plot(ordered141.index, ordered141[variable_name], label='Sensor 141', color='blue')
    plt.plot(ordered142.index, ordered142[variable_name], label='Sensor 142', color='green')
    plt.plot(ordered143.index, ordered143[variable_name], label='Sensor 143', color='purple')
    
    # Set labels and title
    plt.xlabel("Time")
    plt.ylabel(show_name+" in " + unit_name)
    plt.title("Real-time "+show_name+" Change for All Sensors")
    plt.legend(loc='upper center')




def temperature():
    variable_name = "temperature"
    show_name = "Temperature"
    unit_name = "Celcius"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
# Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(i, variable_name,show_name,unit_name), frames=20, interval=1000)
    plt.show()


def humidity():
    variable_name = "humidity"
    show_name = "Humidity"
    unit_name = "Percentage"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
# Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(i, variable_name,show_name,unit_name), frames=20, interval=1000)
    plt.show()


def eco2():
    variable_name = "eCO2Value"
    show_name = "eCO2 Score"
    unit_name = "Parts Per Million"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
# Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(i, variable_name,show_name,unit_name), frames=20, interval=1000)
    plt.show()


def iaqscore():
    variable_name = "iaqScore"
    show_name = "Air Quality Score"
    unit_name = "a 1-150 Scale"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
# Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(i, variable_name,show_name,unit_name), frames=20, interval=1000)
    plt.show()


def iaqpercent():
    variable_name = "iaqPercent"
    show_name = "Air Quality Percent"
    unit_name = "Percent"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
# Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(i, variable_name,show_name,unit_name), frames=20, interval=1000)
    plt.show()


i=0
while i == 0:
    
    get_data_from_csv()

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



            










