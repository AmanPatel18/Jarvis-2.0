import requests
global status
status_list=[]
def init(city):
    api_address="http://api.openweathermap.org/data/2.5/weather?APPID=ec9078566726cc3fe0be78c884222505&q="
    my_city=city
    url=api_address+my_city
    global json_data
    json_data=requests.get(url).json()
    
def status():
    global status
    data1=json_data["weather"][0]
    for key,value in data1.items():
        if key=='main' or key=='description':
            status_list.append(value)
    return status_list

def temp():
    data2=json_data["main"]['temp']
    temp=data2-273
    temp=round(temp,1)
    return temp