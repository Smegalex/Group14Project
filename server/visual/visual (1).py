# Use normal case switch to create option menu and look up tips to make it look more professional
#Find ways to neatly represent data 

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation
import os

def get_data_from_csv(inputarg):

    sensorList = []
    csv_directory = os.path.dirname(os.path.realpath(__file__))
    csv_directory = csv_directory[0:len(csv_directory)-7]
    csv_directory = os.path.join(csv_directory,"computer","data")

    if inputarg == 1:
        print("hi")
        sensorList.append(pd.read_csv(csv_directory+"\sensor140.csv"))
        sensorList.append(pd.read_csv(csv_directory+"\sensor141.csv"))
        sensorList.append(pd.read_csv(csv_directory+"\sensor142.csv"))
        sensorList.append(pd.read_csv(csv_directory+"\sensor143.csv"))
    else:
        sensorList.append(pd.read_csv(csv_directory+"\sensor"+str(inputarg)+".csv"))


    return sensorList

def display_four_graphs(inputarg):
    sensorList = get_data_from_csv(inputarg)
    
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle(f"Sensor Data for {'All Sensors' if inputarg == 1 else f'Sensor {inputarg}'}")
    
    variables = ['temperature', 'humidity', 'eCO2Value', 'iaq']
    titles = ['Temperature (°C)', 'Humidity (%)', 'eCO2 (ppm)', 'Air Quality Score']
    
    for i, (var, title) in enumerate(zip(variables, titles)):
        ax = axs[i // 2, i % 2]
        for j, sensor in enumerate(sensorList):
            sensor_data = sensor.groupby('time')[var].mean()
            ax.plot(sensor_data.index, sensor_data.values, label=f'Sensor {140+j}')
        ax.set_title(title)

        
        ax.set_xlabel('Time')
        ax.legend()
    
    plt.tight_layout()
    plt.show()

def animate(i, variable_name, show_name, unit_name, inputarg):
    sensorList = get_data_from_csv(inputarg)
    # Order data by date for each sensor
    for item in sensorList:
        item = item.groupby("time").sum(numeric_only=True)
    
    # Clear the previous plot
    plt.clf()
    
    # Find the maximum value across all sensors
    
    if inputarg == 1:
        plt.plot(sensorList[0]["time"], sensorList[0][variable_name], label='Sensor 140', color='red')
        plt.plot(sensorList[1]["time"], sensorList[1][variable_name], label='Sensor 141', color='blue')
        plt.plot(sensorList[2]["time"], sensorList[2][variable_name], label='Sensor 142', color='green')
        plt.plot(sensorList[3]["time"], sensorList[3][variable_name], label='Sensor 143', color='purple')
    else:
        print(sensorList)
        plt.plot(sensorList[0]["time"], sensorList[0][variable_name], label='Sensor'+str(inputarg), color='purple')
    
    # Set labels and title
    plt.xlabel("Time")
    plt.ylabel(show_name+" in " + unit_name)
    plt.title("Real-time "+show_name+" Change for All Sensors")
    plt.legend(loc='upper center')


def temperature(inputarg):
    variable_name = "temperature"
    show_name = "Temperature"
    unit_name = "Celcius"
    # Set up the figure
    fig = plt.figure()
# Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(i, variable_name,show_name,unit_name,inputarg), frames=20, interval=1000)
    plt.show()


def humidity(inputarg):
    variable_name = "humidity"
    show_name = "Humidity"
    unit_name = "Percentage"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
# Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(i, variable_name,show_name,unit_name,inputarg), frames=20, interval=1000)
    plt.show()


def eco2(inputarg):
    variable_name = "eCO2Value"
    show_name = "eCO2 Score"
    unit_name = "Parts Per Million"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
# Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(i, variable_name,show_name,unit_name,inputarg), frames=20, interval=1000)
    plt.show()


def iaqscore(inputarg):
    variable_name = "iaqScore"
    show_name = "Air Quality Score"
    unit_name = "a 1-150 Scale"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
# Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(i, variable_name,show_name,unit_name,inputarg), frames=20, interval=1000)
    plt.show()


def iaqpercent(inputarg):
    variable_name = "iaqPercent"
    show_name = "Air Quality Percent"
    unit_name = "Percent"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
# Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(i, variable_name,show_name,unit_name,inputarg), frames=20, interval=1000)
    plt.show()


i=0
while i == 0:
    option1 = input("Please write A for all sensors or the sensor number to target: ")
    if option1.upper() == "A":
        option1 = 1
        get_data_from_csv(option1)
    else:
        get_data_from_csv(int(option1))
    
    print("1. Temperature")
    print("2. Humidity")
    print("3. eCO2")
    print("4. IAQ Score")
    print("5. IAQ Percent")
    print("6. Display 4 graphs")
    option = input("Please select the data type you wish to see: ").lower()

    match option:
        case "temperature" | "1":
            temperature(int(option1))
            i=0

            
    
        case "humidity" | "2":
            humidity(int(option1))
            i=0
            

        case "eco2" | "3":
            eco2(int(option1))
            i=0
            
        case "iaq score" | "4":
            iaqscore(int(option1))
            i=0

        case "iaq percent" | "5":
            iaqpercent(int(option1))
            i=0
        
        case "display 4" | "6":
            display_four_graphs(int(option1))
            i = 0

        case _:
            print("Please ensure a number between 1 -5 or a data type listed above has been entered.")
            i=10



            










