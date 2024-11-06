import serial
import ctypes  # An included library with Python install.
import requests

port = "COM"
url = 'http'
baudrate = 9600
flag = False
        
def MboxInfo(title, text, style):
    ret_val = ctypes.windll.user32.MessageBoxW(0, text, title, style)

def ConfRead():
    global port, url
    file = open('config.txt', "r")
    line = file.readline()
    port = line.rstrip('\n')
    line = file.readline()
    url = line.rstrip('\n')
    file.close()
    
    
# Configure the COM port

try:
    
    # Open the COM port
    ConfRead()
    
    print(port)
    
    ser = serial.Serial(port, baudrate=baudrate)
  
    MboxInfo('ArduinoButtonApp', 'Serial connection established.', 0)
    
    # Read data from the Arduino
    while True:
        # Read a line of data from the serial port      
        line = ser.readline().decode().strip()
       
        if line:
            print("Received:", line)
            if not flag:
                response = requests.post(url, json={'status':'1'})
                print(response)
                print('1')
                flag=True
            else:
                response = requests.post(url, json={'status':'0'})
                print(response)
                print('0')
                flag=False
                

except serial.SerialException as se:
    MboxInfo('ArduinoButtonApp', str(se), 0)


except KeyboardInterrupt:
    pass

finally:
    # Close the serial connection
    if ser.is_open:
        ser.close()
        MboxInfo('ArduinoButtonApp', 'Serial connection lost!', 0)