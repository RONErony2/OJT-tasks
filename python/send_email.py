# 25. Write a program to send a mail notification to customers regarding the arrival of goods
# on a daily basis. The admin email has a separate domain email address owned by your
# company.Do not forget to add cc candidates in customer’s mail.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


email_from = 'jc.cgs.999@gmail.com'
email_password = 'gjrusxnkvntiashs'
email_subject = 'Daily Goods Arrival Notification'

email_body_text = 'Hello,\n\nThis is to inform you that new goods have arrived in our store today.\n\nThank you for your continued patronage.\n\nBest regards,\nSender'
email_body_html =  '<p>This is an <b>HTML</b> message</p>'

recipients = ['moinalikhandevopser@gmail.com']
cc_recipients = ['afwaan3@gmail.com','meghumeghu3@gmail.com']


msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = ', '.join(recipients)
msg['Cc'] = ', '.join(cc_recipients)
msg['Subject'] = email_subject
msg.attach(MIMEText(email_body_text, 'plain'))
msg.attach(MIMEText(email_body_html, 'html'))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_from, email_password)

server.sendmail(email_from, recipients + cc_recipients, msg.as_string())

print('Email notification sent successfully!')

server.quit()