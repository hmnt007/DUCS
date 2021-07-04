import os
import datetime
import requests
import json
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_ID')
PASS = os.environ.get('EMAIL_PASS')
sender = EMAIL_ADDRESS
recievers = ['hemant.mca19.du@gmail.com', EMAIL_ADDRESS]

subject = "Cowin Bookings.."

body = '''
Alert..!!!
Cowin booking slots are available in you area.
Book your slots immediately...
The Details for the same are as following..!!!

'''
message = f'Subject: {subject}\n\n{body}'
def notifier():
    print("Sending mail to the recipients...")
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            #smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp.login(EMAIL_ADDRESS, PASS)  
            smtp.sendmail(sender, recievers, message)
                   
            print ("Successfully sent email")
    except:
        print ("Error: unable to send email")


def main():
    print("Vaccine Notifier is looking for available slots...\n")
    try :
        print("Checking Availabilities...")
        checkAvailability()
    except:
        print("No available slots.. Try again!!")


def checkAvailability():
    today = datetime.datetime.today()
    dateList = [today + datetime.timedelta(days=x) for x in range(10)]
    actual_dates = [i.strftime("%d-%m-%Y") for i in dateList]
    for d in  actual_dates:
        print(d)
    pinsList = [110005]
    for pin_code in pinsList :
        for date in dateList :
            getSlotsForDate(pin_code, date)

# def addDates():
#     today = datetime.datetime.today()
#     dateList = [today + datetime.timedelta(days=x) for x in range(10)]
#     actual_dates = [i.strftime("%d-%m-%Y") for i in dateList]

def getSlotsForDate(pin_code, date):
    print("Connecting to cowin website...")
    URL =      "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pin_code, date)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
              'accept': 'application/json',
              'Accept-Language': 'hi_IN'} 
    response = requests.get(URL, header)
    print(response)
    if(response.ok) :
        print("getting data from cowin...")
        resp_json = json.loads(response.text)['centers']
        if resp_json is not None:
            print("data found...\n")
            for center in resp_json['centers'] :
                for session in center['sessions'] :
                    message = ""
                    if (session["available_capacity"] >= 0 and session["fee_type"]=="Free") :                 
                        message+=('Pincode: ' + str(pin_code)+"\n")
                        message+=(f'Available on: {date}'+"\n")
                        message+=("\t"+ center["name"]+"\n")
                        message+=("\t"+ center["block_name"]+"n")
                        message+=("\t Availablity : "+ str(session["available_capacity"])+"\n")
                        if(session["vaccine"] != ''):
                            message+=("\t Vaccine type: "+session["vaccine"]+"\n")
                        message+="\n"
            
            notifier()

        else:
            print('No response from the server!!!')

if __name__ == "__main__":
    main()
