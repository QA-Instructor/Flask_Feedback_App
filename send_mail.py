import smtplib
from email.mime.text import MIMEText
# allows us to send html and text emails

def send_mail(customer, engineer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '1ec1718bb1dcb6'
    password = '934d8c2bc3cd08'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li>" \
              f"<li>Engineer: {engineer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"
    sender_email = 'victoria@sky.com'
    receiver_email = 'email2@sky.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Sky Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
