from django.core.mail import send_mail

def send_mail_pnc():
    send_mail(
        subject = 'That\'s your subject',
        message = 'That\'s your message body',
        from_email = 'phuongnam.kimnt1@fpt.net',
        recipient_list = ['kimnguyen035171@gmail.com',],
        auth_user = 'phuongnam.kimnt1@fpt.net',
        auth_password = 'K@12345abcd',
        fail_silently = False
    )