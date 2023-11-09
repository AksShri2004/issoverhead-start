import requests
from datetime import datetime
import smtplib
import time

while True:
    time.sleep(60)

    MY_LAT = 23.181467 # Your latitude
    MY_LONG = 79.986404 # Your longitude

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    def pos_near():
        if (iss_latitude == MY_LAT + 5 or iss_latitude== MY_LAT - 5) and (iss_longitude == MY_LONG + 5 or iss_longitude == MY_LONG - 5):
            return True


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour

    #If the ISS is close to my current position
    if pos_near() and sunrise> hour > sunset :
        my_email = "aakksshhaatt4@gmail.com"
        password = "yqym mupv rrbr qrot"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='shrivastavaakshat2004@gmail.com',
                msg="LOOK UP"
            )
    print("code is runned")
    # and it is currently dark

    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.





