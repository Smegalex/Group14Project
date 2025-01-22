from bme688 import *

init_sensor()
init_gas_sensor()


def read_metrics(sensor_id):
    read_data_registers()

    temp = calc_temperature()
    humidity = calc_humidity()
    iaqScore, iaqPercent, eCO2Value = calc_air_quality()

    return {
        "temperature": temp,
        "humidity": humidity,
        "eCO2Value": eCO2Value,
        "iaqScore": iaqScore,
        "iaqPercent": iaqPercent,
    }
