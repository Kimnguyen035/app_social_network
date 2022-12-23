from django.core.mail import send_mail
from configs.variable_system import *
from configs.variable_send_mail import *
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from anymail.message import attach_inline_image_file


def send_mail_pnc():
    send_mail(
        subject = MESSAGE_EMAIL['subject'],
        message = MESSAGE_EMAIL['body'],
        from_email = USER_SEND_MAIL['from'],
        recipient_list = USER_SEND_MAIL['recipient_list'],
        auth_user = USER_SEND_MAIL['from'],
        auth_password = USER_SEND_MAIL['password_mail'],
        fail_silently = USER_SEND_MAIL['fail_silently'],
        html_message='<html><body> <img src="test.png"> </body></html>'
    )
    
def send_email_message():
    email = EmailMessage(
            'Hello',
            'You have free time? Please take a look at this file.',
            USER_SEND_MAIL['from'],
            USER_SEND_MAIL['recipient_list']
    )
    email.attach_file('/home/an/Downloads/test.png')
    email.send()
    
def multi_mail():
    subject, from_email, to = 'hello', 'phuongnam.kimnt1@fpt.net', 'kimnguyen035171@gmail.com'
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, USER_SEND_MAIL['recipient_list'])
    cid = attach_inline_image_file(msg, '/home/an/Downloads/test.png')
    html_content = '<div class="container-fluid"> <div class="row"><div class="col-sm-2"><center><img src="{% static \'test.png\' %}" class="responsive-img" style="max-height:150px"/></center></div><div class="col-sm-10"><center><h2>Blog Làm từ Python Django</h2></center></div></div></div>'
    msg.attach_alternative(html_content, "text/html")
    msg.send(USER_SEND_MAIL['fail_silently'][0])