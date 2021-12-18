

import requests



KEY = 'b070e72a847ad84bd5130c55a63f2f04' # key for API
URL = 'https://api.openweathermap.org/data/2.5/weather' #API URL

def getInput(): # function for getting user input
    print("Select one option from which you want to find current weather conditions\n")
    choice = input('Enter 1 for city name and 2 for zip code: ')
    choice = int(choice)
    if(choice==1): # check whether user wants to use city name or zip code
        city = input("Enter city name: ")
        return (city,choice)
    elif(choice==2):
        zipcode = input("Enter zip code: ")
        return (zipcode,choice)
    else:
        return ("error","")



def findData(reqInput, choice,PARAMS): # function where to find data according to user input
    if(choice==1): # adding key value to params according to user choice
        PARAMS["q"] = reqInput
    else:
        PARAMS["zip"] = reqInput
    try:
        req = requests.get(url = URL, params=PARAMS) # api hit for data
        print("Connection established successfully.")
    except:
        print("Connection failed.")
    return req.json() # getting data in json

def validateInput(data): # function to validate data and print the result if we get data
#     print(data)
    if data['cod']=='404': # checking if the data is incorrect 
        print("Please enter valid data")
    elif data['cod']==200: # check if we get data and print all the necessary data
        print("----------------------------------------")
        print("Country: ",data['sys']['country'], " \n")
        print("City: ",data['name'], " \n")
        print("Weather Description: ",data['weather'][0]['main'],"\n")
        print("Temperature: ",data['main']['temp'], " Celsius \n")
        print("Feels Like: ",data['main']['feels_like'], " Celsius \n")
        print("Atmospheric Pressure: ",data['main']['pressure'], "\n")
        print("Humidity: ",data['main']['humidity'], " \n")
        print("Wind Speed: ",data['wind']['speed'], " meter/sec \n")
        print("----------------------------------------")
    else:
        print("Something went wrong on API side.")

if __name__ == "__main__":
    check = 1
    while(check==1):
        PARAMS = {'appid':KEY,"units":"metric","mode":"json"}
        reqInput,choice = getInput()
        if(reqInput!="error"):
            data = findData(reqInput,choice,PARAMS)
            validateInput(data)
        else:
            print("Your selected option is incorrect")
        
        endProg = input("Do you want continue?(y/n): ")
        if(endProg.lower()=='y'):
            pass
        else:
            check=2
