import matplotlib.pyplot as plt
import pandas as pd
import datetime
import matplotlib.animation as animation
import os

VALID_SENSORS = [141, 142, 143, 144]
DATATYPE_CONVERSION = {
    "1": "temperature",
    "temperature": "temperature",
    "temp": "temperature",
    "1.": "temperature",

    "2": "humidity",
    "humidity": "humidity",
    "humid": "humidity",
    "2.": "humidity",

    "3": "eco2",
    "eco2": "eco2",
    "co2": "eco2",
    "3.": "eco2",

    "4": "iaq score",
    "iaq score": "iaq score",
    "4.": "iaq score",

    "5": "iaq percent",
    "iaq percent": "iaq percent",
    "iaq": "iaq percent",
    "iaq percentage": "iaq percent",
    "5.": "iaq percent",

    "6": "display 4",
    "display 4": "display 4",
    "all 4": "display 4",
    "4 graphs": "display 4"
}
VALID_DATATYPES = ["temperature", "humidity",
                   "eco2", "iaq score", "iaq percent", "display 4"]
RED = "\033[1;31m"
GRAY = "\033[0m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"


def print_allowed_datatypes() -> None:
    print("1. Temperature")
    print("2. Humidity")
    print("3. eCO2")
    print("4. IAQ Score")
    print("5. IAQ Percent")
    print("6. Display 4 graphs (Temp, Humidity, eCO2, IAQ Percent)")


def add_csv_data(filename: str, verbose: bool = False) -> pd.DataFrame | None:
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        if verbose:
            print(f"{RED}File {filename} haven't been found.{GRAY}")
    except pd.errors.EmptyDataError:
        if verbose:
            print(f"{RED}File {filename} is empty.{GRAY}")


def get_data_from_csv(inputarg: int | list, verbose: bool = False) -> dict:
    sensorList = {}
    csv_directory = os.path.dirname(os.path.realpath(__file__))
    csv_directory = csv_directory[0:len(csv_directory)-7]
    csv_directory = os.path.join(csv_directory, "dataProcessing", "data")

    if isinstance(inputarg, list):
        for sensor in inputarg:
            sensorList[str(sensor)] = add_csv_data(
                csv_directory+"\\sensor"+str(sensor)+".csv", verbose=verbose)
    elif inputarg == 140:
        # if verbose:
        #     print("hi")
        sensorList['141'] = add_csv_data(
            csv_directory+"\\sensor141.csv", verbose=verbose)
        sensorList['142'] = add_csv_data(
            csv_directory+"\\sensor142.csv", verbose=verbose)
        sensorList['143'] = add_csv_data(
            csv_directory+"\\sensor143.csv", verbose=verbose)
        sensorList['144'] = add_csv_data(
            csv_directory+"\\sensor144.csv", verbose=verbose)
    else:
        sensorList[str(inputarg)] = add_csv_data(
            csv_directory+"\\sensor"+str(inputarg)+".csv", verbose=verbose)
    sensorList = {key: value for key,
                  value in sensorList.items() if value is not None}
    return sensorList


def display_four_graphs(inputarg: int | list) -> None:
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    title = "Sensor Data for "
    if inputarg == 140:
        title += "all sensors."
    elif isinstance(inputarg, list):
        title += f'sensors {", ".join(str(inputarg))}.'
    else:
        title += f'sensor {inputarg}.'

    fig.suptitle(title)
    fig = animation.FuncAnimation(fig, lambda i: animate_four_graphs(
        i, inputarg, axs), frames=20, interval=1000)
    plt.show()


def animate_four_graphs(i, inputarg: int | list, axs) -> None:
    sensorList = get_data_from_csv(inputarg)

    variables = ['temperature', 'humidity', 'eCO2Value', 'iaqPercent']
    titles = ['Temperature (°C)', 'Humidity (%)',
              'eCO2 (ppm)', 'Air Quality Percentage']

    for i, (var, title) in enumerate(zip(variables, titles)):
        ax = axs[i // 2, i % 2]
        ax.clear()
        for name, sensor in sensorList.items():
            sensor_data = sensor.groupby('time')[var].mean()
            ax.plot(to_datetime(sensor_data.index),
                    sensor_data.values, label=name)
        ax.set_title(title)

        ax.set_xlabel('Time')
        ax.legend()
    plt.tight_layout()
    plt.gcf().autofmt_xdate()
    plt.subplots_adjust(bottom=0.12)


def to_datetime(arr: list) -> datetime:
    return [datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S") for time in arr]


def animate(i, variable_name: str, show_name: str, unit_name: str, inputarg: int | list) -> None:
    sensorList = get_data_from_csv(inputarg)
    # Order data by date for each sensor
    for item in sensorList.values():
        item = item.groupby("time").sum(numeric_only=True)

    # Clear the previous plot
    plt.clf()
    colorList = ["red", "blue", "green", "purple", "orange"]

    # Find the maximum value across all sensors
    for name, sensor in sensorList.items():
        plt.plot(to_datetime(
            sensor["time"]), sensor[variable_name], label=name, color=colorList[0])
        colorList.pop(0)

    # Set labels and title
    plt.gcf().autofmt_xdate()
    plt.xlabel("Time")
    plt.ylabel(show_name+" in " + unit_name)
    plt.title("Real-time "+show_name+" Change for All Sensors")
    plt.legend(loc='upper center')


def temperature(inputarg: int | list) -> None:
    variable_name = "temperature"
    show_name = "Temperature"
    unit_name = "Celcius"
    # Set up the figure
    fig = plt.figure()
    # Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(
        i, variable_name, show_name, unit_name, inputarg), frames=20, interval=1000)
    plt.show()


def humidity(inputarg: int | list) -> None:
    variable_name = "humidity"
    show_name = "Humidity"
    unit_name = "Percentage"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
    # Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(
        i, variable_name, show_name, unit_name, inputarg), frames=20, interval=1000)
    plt.show()


def eco2(inputarg: int | list) -> None:
    variable_name = "eCO2Value"
    show_name = "eCO2 Score"
    unit_name = "Parts Per Million"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
    # Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(
        i, variable_name, show_name, unit_name, inputarg), frames=20, interval=1000)
    plt.show()


def iaqscore(inputarg: int | list) -> None:
    variable_name = "iaqScore"
    show_name = "Air Quality Score"
    unit_name = "a 1-150 Scale"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
    # Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(
        i, variable_name, show_name, unit_name, inputarg), frames=20, interval=1000)
    plt.show()


def iaqpercent(inputarg: int | list) -> None:
    variable_name = "iaqPercent"
    show_name = "Air Quality Percent"
    unit_name = "Percent"
    # Set up the figure
    fig = plt.figure(figsize=(12, 6))
    # Create the animation
    fig = animation.FuncAnimation(fig, lambda i: animate(
        i, variable_name, show_name, unit_name, inputarg), frames=20, interval=1000)
    plt.show()


def display(options: list | int, datatype: str) -> None:
    try:
        datatype = DATATYPE_CONVERSION[datatype]
    except KeyError:
        print(
            f"{RED}Please ensure correct data type is selected.{GRAY}")
        return None
    match datatype:
        case "temperature":
            temperature(options)
        case "humidity":
            humidity(options)
        case "eco2":
            eco2(options)
        case "iaq score":
            iaqscore(options)
        case "iaq percent":
            iaqpercent(options)
        case "display 4":
            display_four_graphs(options)


if __name__ == "__main__":
    while True:
        options = input(
            f"{WHITE}Please write '/a' for all sensors OR sensor numbers separated by whitespace to target OR '/s' to stop: {GRAY}").strip().lower()
        options = list(set(options.split(" ")))
        if " " in options:
            options.remove(" ")
        if len(options) == 1:
            options = options[0]
            if options == "/a" or options == "140":
                options = 140
                get_data_from_csv(140, verbose=True)
            elif options == "/s":
                print(f"{YELLOW}Program stopped.{GRAY}")
                break
            else:
                try:
                    options = int(options)
                    if not options in VALID_SENSORS:
                        raise ValueError
                    get_data_from_csv(options, verbose=True)
                except ValueError:
                    print(f"{RED}Incorrect argument passed for the sensor number: {
                          GRAY}{options}.")
                    continue
        else:
            try:
                for i, sensor in enumerate(options):
                    sensor = sensor.strip()
                    try:
                        sensor = int(sensor)
                        if not sensor in VALID_SENSORS:
                            raise ValueError
                        options[i] = sensor
                    except ValueError:
                        print(f"{RED}Incorrect argument passed for the sensor number: {
                              GRAY}{sensor}.")
                        raise ValueError
                get_data_from_csv(options, verbose=True)
            except ValueError:
                continue

        print_allowed_datatypes()
        datatype = input(f"{WHITE}Please select the data type you wish to see: {
                         GRAY}").lower().strip()

        try:
            datatype = DATATYPE_CONVERSION[datatype]
        except KeyError:
            print(
                f"{RED}Please ensure a number between 1-6 or a data type listed above has been entered.{GRAY}")
            continue

        display(options, datatype)
