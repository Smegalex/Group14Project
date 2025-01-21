from bme688 import *
from OLED import *
init_sensor()
init_gas_sensor()
def getData(deviceID):
    read_data_registers()
    temp = calc_temperature()
    humidity = calc_humidity()
    iaqScore, iaqPercent, eCO2Value = calc_air_quality()
    show("Temperature: {} C".format(temp), 0)
    show("Humidity: {} %".format(humidity), 1)
    show("IAQ Score: {}".format(iaqScore), 2)
    show("IAQ Percent: {} %".format(iaqPercent) , 3)
    show("eCO2 Value: {}".format(eCO2Value) + " ppm", 4)
    return {"deviceID":deviceID,"temperature":temp,"humidity":humidity,"eCO2Value":eCO2Value,"iaqScore":iaqScore}
    