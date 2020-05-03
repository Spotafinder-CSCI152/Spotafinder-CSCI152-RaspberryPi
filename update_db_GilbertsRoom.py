import pyrebase
from random import seed
from random import randint
import time as ti
import csv
from datetime import datetime, timedelta
import serial
import json

port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=11.0)


class updateData:
        def __init__(self, EEdb, Ldb):
                self.EEdb = EEdb
                self.Ldb = Ldb
        
        def send(self):
                eeSD = countDevices()
                x = {'occupancy': eeSD}
                data = readSerialData()
                if data != None:
                    x.update(data)
                    print(x)
                EEdata = {"Engineering East/rooms/GilbertsRoom":x}
                self.EEdb.update(EEdata)
                
                
                
class configureDB:
        def __init__(self, EEdb, Ldb):
                self.EEdb = EEdb
                self.Ldb = Ldb
        
        def config(self):
                config = {
                  "apiKey": "AIzaSyAzclOJusoyXpvyB9GHpk4_3ddwtOm-36w",
                  "authDomain": "spotifinder-c42a6.firebaseapp.com",
                  "databaseURL": "https://spotafinder-c42a6.firebaseio.com/",
                  "storageBucket": "spotifinder-c42a6.appspot.com"
                }

                firebase = pyrebase.initialize_app(config)
                self.EEdb = firebase.database()
                self.Ldb = firebase.database()


def countDevices():
        devices = 0
        x = []
        flag = False
        with open('outputSniffGilbertsRoom-01.csv',newline='', encoding='utf-8') as csvfile:
                cr = csv.DictReader(csvfile)
                t = datetime.today()- timedelta(minutes=5)
                for row in cr:
                        for j in row.items():
                                if flag:
                                        try:
                                            d = datetime.strptime(j[1][2], " %Y-%m-%d %H:%M:%S")
                                        except IndexError:
                                            pass
                                        if d > t:
                                                x.append(int(j[1][3]))
                                if j[1][0] == 'Station MAC':
                                        flag = True
                
                for i in x:
                    if i >= -60:
                        devices += 1
                return devices

def readSerialData():
    rcv = port.readline()
    try:
        data = json.loads(rcv.decode("utf-8"))
        #print(data)
        return data
    except json.decoder.JSONDecodeError:
        print("No Serial data")
        return None


def main():
        c = configureDB('eedb', 'ldb')
        c.config()
        o = updateData(c.EEdb, c.Ldb)
        seed(1)
        while True:
                o.send()
                ti.sleep(60)
                

if __name__ == '__main__':
        main()

        
