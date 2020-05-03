import serial
import json

port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=11.0)

#while True:
#    rcv = port.readline()
#    data = json.loads(rcv.decode("utf-8"))
#    #print(type(rcv))
#    print(data)
    
def readSerialData():
    rcv = port.readline()
    try:
        data = json.loads(rcv.decode("utf-8"))
        print(data)
        return data
    except json.decoder.JSONDecodeError:
        print("No Serial data")
        return None
    


readSerialData()