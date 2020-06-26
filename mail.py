#!/bin/bash/python3
import smtplib

s=smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login("satyamsingh1402@gmail.com","Singh@1402")

subject1 = 'Important'

message1 = "Your code has been failed, please debug it asap."

s.sendmail("satyamsingh1402@gmail.com","satyamkr.gaya@gmail.com",message1)

s.quit()
