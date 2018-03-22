#all imports
import smtplib  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText                    
from email.mime.application import MIMEApplication
from os.path import basename
import email
import email.mime.application


#array of emails
with open("emails.txt", "r") as ins:
    array_email = []
    for line in ins:
        array_email.append(line.strip('\n'))

#array of picture numbers
with open("photonumbers.txt", "r") as ins:
    array_photo = []
    for line in ins:
        array_photo.append("IMG_" + line.strip('\n') +   ".jpg")

#html body
f = open("body.txt", "r")
html = f.read()
thebody= MIMEText(html, 'html')

#loop to send all emails
for i in range(len(array_email)):

    #spen picture
    filename = array_photo[i] 
    fp= open(filename,'rb')
    att = email.mime.application.MIMEApplication(fp.read(),_subtype="jpg")
    fp.close()
    att.add_header('Content-Disposition','attachments.',filename=filename)

    #attach picture an html to the body
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "PUTSUBJECTHERE" #email subject
    msg['From'] = "PUTEMAILHERE" #from email
    msg.attach(att)
    msg.attach(thebody)

    #connect to server
    s = smtplib.SMTP()
    s.connect('smtp.gmail.com',587) #gmail portal
    s.starttls()

    #send email
    msg['To'] = array_email[i]
    s.login('PUTEMAILHERE','PUTPASSWORDHERE') #login information
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
