# Group14Project

Project Plan
-	4 Kitronik sensors with unique personal ID
-	Spare microbits can be used to extend signals
-	Send data to one microbit acting as a server
o	Data in form of a dictionary : {"deviceID":deviceID,"temperature":temp,"humidity":humidity,     
    "eCO2Value":eCO2Value"iaqScore":iaqScore,"iaqPercent":iaqPercent}
o	Server requests data from the sensors
	Device ID is a string (“sensor140”, “sensor141” …)
	server14S, server14C ID’s for the servers
