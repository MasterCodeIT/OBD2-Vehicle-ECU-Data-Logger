import obd
import time

obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.Async(portstr="COM7",baudrate=19200, fast=False) # connect to the first port in the list

# a callback that prints every new value to the console
#RPM
def new_rpm(r):
    print("RPM: ",r.value)
    print("\t")
#SPEED
def new_speed(r):
    print("SPEED: ",r.value)
    print("\t")
#COOLANT TEMPERATURE
def new_coolant_temperature(r):
    print("Coolant temperature: ",r.value)
    print("\t")
#THROTTLE POSITION
def new_throttle_position(r):
    print("THROTTLE POSITION: ",r.value)
    print("\t")

#FUEL_LEVEL
def new_fuel_level(r):
    print("Fuel level: ",r.value)
    print("\t")

while not connection.is_connected():
    connection.close()
    print("...waiting for connection ...")
    #time.sleep(0.5)
    """" TRATAR DE OBTENER SOLO EL PUERTO TRATADO COMO STRING"""
    connection = obd.Async(portstr="COM7",baudrate=19200, fast=False) # connect to the first port in the list
    
print("---- CONNECTED to OBD-II DEVICE ----")


connection.watch(obd.commands.RPM, callback=new_rpm)
connection.watch(obd.commands.SPEED, callback=new_speed)
connection.watch(obd.commands.COOLANT_TEMP, callback=new_coolant_temperature)
connection.watch(obd.commands.THROTTLE_POS, callback=new_throttle_position)
connection.watch(obd.commands.FUEL_PRESSURE, callback=new_fuel_level)
connection.start()

time.sleep(600)
connection.stop()