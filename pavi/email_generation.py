import smtplib
import os
import json
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.message import MIMEMessage
from email.mime.text import MIMEText

from email.header  import Header

def getSummary(filename , data_dict):
    with open(filename ,encoding='utf-8') as html_file:
        template = html_file.read()
        html_data = template.format(**data_dict)
        return html_data

def attach_image(img_dict):
    with open(img_dict['path'], 'rb') as file:
        msg_image = MIMEImage(file.read(), name = os.path.basename(img_dict['path']))
    msg_image.add_header('Content-ID', '<{}>'.format(img_dict['cid']))
    return msg_image

def send_email(msg, from_email, from_gmail_pwd, to_email):
    with smtplib.SMTP_SSL('smtpout.secureserver.net' , 465) as mailServer :#port for ssl
        mailServer.ehlo()
        mailServer.login(from_email , from_gmail_pwd)
        mailServer.sendmail(from_email , to_email , msg.as_string())

def generate_individual_email(filename,data,firstname,from_email,to_email,img_delta_hr,img_delta_spo2):
    msg = MIMEMultipart('related')
    msg['Subject'] = Header(u'Control Compare Stats of ' + firstname , 'utf-8')
    msg['From'] = from_email
    msg['To'] = to_email

    msg_alternative = MIMEMultipart('alternative')
    msg_text = MIMEText(u'Images not found', 'plain', 'utf-8')
    msg_alternative.attach(msg_text)
    msg.attach(msg_alternative)
    #adding the html content
    msg_html = 'Greetings of the day' + firstname +','+'<br/>'
    msg_html += getSummary(filename,data)

    msg_html += u'<div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(
        alt=html.escape(img_delta_hr['title'], quote=True), **img_delta_hr)
    msg_html += u'<div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(
        alt=html.escape(img_delta_spo2['title'], quote=True), **img_delta_spo2)
    
    msg_html = MIMEText(msg_html , 'html' , 'utf-8')
    msg_alternative.attach(msg_html)
    msg.attach(attach_image(img_delta_hr))
    msg.attach(attach_image(img_delta_spo2))
    return msg


def document_email(filename,data,from_email,to_email,img_delta_hr,img_delta_spo2):
    msg = MIMEMultipart('related')
    msg['Subject'] = Header(u'Control Compare Stats for All Users', 'utf-8')
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Cc'] = ' ybobra@omnyk.com, mgraghuveer19@gmail.com,kavananagesh17@gmail.com'
    msg_alternative = MIMEMultipart('alternative')
    msg_text = MIMEText(u'Images not found', 'plain', 'utf-8')
    msg_alternative.attach(msg_text)
    msg.attach(msg_alternative)
    msg_html = 'Hello ,' + "<br/>"
    msg_html+= getSummary(filename,data)
    msg_html += u'<div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(
        alt=html.escape(img_delta_hr['title'], quote=True), **img_delta_hr)
    msg_html += u'<div dir="ltr">''<img src="cid:{cid}" alt="{alt}"><br></div>'.format(
        alt=html.escape(img_delta_spo2['title'], quote=True), **img_delta_spo2)
    msg_html = MIMEText(msg_html, 'html', 'utf-8')
    msg_alternative.attach(msg_html)
    msg.attach(attach_image(img_delta_hr))
    msg.attach(attach_image(img_delta_spo2))
    return msg

    


