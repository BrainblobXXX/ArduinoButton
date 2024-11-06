import requests

url = 'http'
flag = False
        
def ConfRead():
    global port, url
    file = open('TestConfig.txt', "r")
    line = file.readline()
    url = line.rstrip('\n')
    print(url)
    file.close()
    
try:
    
    ConfRead()
    X = input("Нажмите ввод для Click")
    print(X)
    
    while True:
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
                
except KeyboardInterrupt:
    pass

finally:
    # Close the serial connection
    print("Bye!")