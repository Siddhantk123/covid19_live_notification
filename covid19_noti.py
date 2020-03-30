import requests
from plyer import notification
from bs4 import BeautifulSoup
import time

def notifyMe(title, message): #To Show The Notification
    notification.notify(
        title= title,
        message = message,
        app_icon = "virus.ico",
        timeout = 20 #Timeout Settings In Seconds
    )

def webData(url): #Getting The Data From The Website
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        html_doc = webData('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(html_doc, 'html.parser') #Parsing The Data
        mystr = ""

        for tr in soup.find_all ('tbody')[9].find_all('tr'):
            mystr += tr.get_text() #Converting the Parsed Data to a String 
            
        
         
        mystr = mystr[1:]
        
        
        
        
        myList = (mystr.split("\n")) 
        #print(myList)
        
       
        
        
        
        
        
        

        
        states = ['Delhi','Uttar Pradesh', 'Maharashtra',] # Enter Your State Name Here (Dont Enter More Than 5 States)
        length=len(myList)
        for item in  range (length):
            #dataList = (item.split('\n'))
            #print(dataList)
            

            if myList[item] in states:
                notify_title= 'Cases of Covid-19 In India'
                notify_text= f" State: {myList[item]}\n Indian Cases : {myList[item+1]} \n Cured : {myList[item+3]}\n Deaths : {myList[item+4]}"
                notifyMe(notify_title, notify_text)
                time.sleep(2)
        time.sleep(3600)    #Loop For 1 Hour (1 hour = 3600 seconds)            
                
                


    
    
