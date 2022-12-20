from django.core.mail import send_mail
from configs.variable_system import *
from configs.variable_send_mail import *
from django.core.mail import EmailMessage

def send_mail_pnc():
    send_mail(
        subject = MESSAGE_EMAIL['subject'],
        message = MESSAGE_EMAIL['body'],
        from_email = USER_SEND_MAIL['from'],
        recipient_list = USER_SEND_MAIL['recipient_list'],
        auth_user = USER_SEND_MAIL['from'],
        auth_password = USER_SEND_MAIL['password_mail'],
        fail_silently = USER_SEND_MAIL['fail_silently']
    )
    
def send_email_message():
    email = EmailMessage(
            'Hello',
            'You have free time? Please take a look at this file.',
            USER_SEND_MAIL['from'],
            USER_SEND_MAIL['recipient_list'],
    )
    email.attach_file('/home/an/Downloads/CV-TESTER.pdf')
    email.send()