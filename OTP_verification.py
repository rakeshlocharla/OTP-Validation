import random
import smtplib

digits = "0123456789"
OTP = "".join([random.choice(digits) for i in range(6)])


otp = OTP + " is your OTP"
msg = otp

s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()

# gmail account and password that send the opt code to user gmail
s.login("techg5190@gmail.com", "gwthjojfzbeqirvt")

emailid = input("Enter your email: ")
s.sendmail("techg5190@gmail.com", emailid, msg)

a = input("Enter Your OTP >>: ")
# verify the code
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
