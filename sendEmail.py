import smtplib
import conf
def sendEmail(msg,recieverEmail):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(conf.email,conf.pas)
		server.sendmail(conf.email, recieverEmail ,msg)
		server.quit()
		print("Email was sucssesfully sent")
	except:
		print("Error in sending the email")

msg = "YOURMESSAGEHERE"
recieverEmail = "RECIEVEREMAIL@gmail.com"
sendEmail(msg,recieverEmail)