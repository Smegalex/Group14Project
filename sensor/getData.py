from bme688 import *
from OLED import *
init_sensor()
init_gas_sensor()
def getData(deviceID):
    read_data_registers()
    temp = calc_temperature()
    humidity = calc_humidity()
    iaqScore, iaqPercent, eCO2Value = calc_air_quality()
    show("Device ID: {}".format(deviceID) , 0)
    show("Temperature: {} C".format(temp), 1)
    show("Humidity: {} %".format(humidity), 2)
    show("IAQ Score: {}".format(iaqScore), 3)
    show("IAQ Percent: {} %".format(iaqPercent) , 4)
    show("CO2 Level: {}".format(eCO2Value),5)
    show("Reading Successful.".format(iaqPercent) , 6)
    return {"deviceID":deviceID,"temperature":temp,"humidity":humidity,"eCO2Value":eCO2Value,"iaqScore":iaqScore,"iaqPercent":iaqPercent}
    