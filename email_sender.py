import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = '<your name>'
email['to'] = '<email addres>'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': '<nsme of the person>'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('<your email>', 'your password')
  smtp.send_message(email)
  print('all good boss!')