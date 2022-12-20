from django.core.mail import send_mail
from configs.variable_system import *

def send_mail_pnc():
    send_mail(
        subject = 'COPY THOI',
        message = 'Trong trận làm tụi tui đau tim. Chiến thắng làm chúng tui ná thở, ko dám bỏ đi xả nước cứu thân luôn 😂 Còn tấm ảnh này nhìn thật xúc động, quá đủ cho 1 chiến thắng tự hào 🥰',
        from_email = USER_SEND_MAIL['from'],
        recipient_list = USER_SEND_MAIL['recipient_list'],
        auth_user = USER_SEND_MAIL['from'],
        auth_password = USER_SEND_MAIL['password_mail'],
        fail_silently = USER_SEND_MAIL['fail_silently']
    )