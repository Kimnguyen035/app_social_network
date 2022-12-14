from django.core.mail import send_mail
from configs.variable_system import *

def send_mail_pnc():
    send_mail(
        subject = 'That\'s your subject',
        message = 'That\'s your message body',
        from_email = USER_SEND_MAIL['from'],
        recipient_list = USER_SEND_MAIL['recipient_list'],
        auth_user = USER_SEND_MAIL['from'],
        auth_password = USER_SEND_MAIL['password_mail'],
        fail_silently = USER_SEND_MAIL['fail_silently']
    )