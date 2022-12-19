from django.core.mail import send_mail
from configs.variable_system import *

def send_mail_pnc():
    send_mail(
        subject = 'TAO TEST NHA',
        message = 'XIN BAN DUNG CO CHUI MINH NHA HAHA',
        from_email = USER_SEND_MAIL['from'],
        recipient_list = USER_SEND_MAIL['recipient_list'],
        auth_user = USER_SEND_MAIL['from'],
        auth_password = USER_SEND_MAIL['password_mail'],
        fail_silently = USER_SEND_MAIL['fail_silently']
    )