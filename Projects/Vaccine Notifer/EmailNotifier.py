import smtplib
import os
EMAIL = os.environ.get('EMAIL_ID1')
PASS  = os.environ.get('EMAIL_PASS1')
sender = 'hemantkumar0607@gmail.com'
receivers = ['hemant.mca19.du@gmail.com']

message = """From: From Hemant Kumar <hemant.mca19.du@gmail.com>
To: To Hemant <hemantkumar0607@gmail.com>
Subject: Cowin Booking Available

Bookings are open.
"""
def notify():
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL, PASS)  
            smtp.sendmail(sender, receivers, message)
                   
            print ("Successfully sent email")
    except:
        print ("Error: unable to send email")
notify()
