import csv
import serial
import datetime

ser=serial.Serial('/dev/ttyACM0',9600)
with open('coordinate.csv','a',newline='')as csvfile:
    fieldnames=['timestamp','x','y','z']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    #writer.writeheader()
    while True:
        data1=ser.readline().decode().strip()
        data2=ser.readline().decode().strip()
        data3=ser.readline().decode().strip()
        timestamp=datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        writer.writerow({'timestamp':timestamp,'x':data1,'y':data2,'z':data3})
        csvfile.flush()