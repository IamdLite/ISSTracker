from time import sleep
from pendulum import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 3.95376 #your longitude
MY_LONG = 11.51668 #your latitude
MY_EMAIL = "example1@gmail.com" #your email
MY_PASSWORD = "password" #your password



def is_night():
    parameters ={
    "lat": MY_LAT, 
    "long": MY_LONG,
    "formatted": 0,}

    response_sunrise_sunset = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sunrise_sunset.raise_for_status()
    data_time = response_sunrise_sunset.json()

    sunrising_hour = float(data_time["results"]["sunrise"].split("T")[1].split(":")[0])
    sunsetting_hour = float(data_time["results"]["sunset"].split("T")[1].split(":")[0])
    current_hour = int(datetime.now().hour)
    if current_hour >= sunsetting_hour or current_hour <= sunrising_hour:
        return True



def is_iss_overhead():
    response_iss = requests.get(url= "http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data = response_iss.json()
    current_iss_latitude = data["iss_position"]["latitude"]
    current_iss_longitude = data["iss_position"]["longitude"]
    if MY_LAT - 5 <= current_iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= current_iss_longitude <= MY_LONG + 5:
        return True


while True:
    sleep(60)   
    if is_night and is_iss_overhead: 
        # Implementing the email notifier
        connection = smtplib.SMTP("smtp.google.com", 587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs="example@gmail.com",
            msg= "Subject:The ISS is above in the sky\n\nGo and look the wonderful satellite riding over your location"
        )
        
    
