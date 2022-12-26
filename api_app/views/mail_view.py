from .views import *
from django.core.mail import send_mail
from email.mime.image import MIMEImage
from pathlib import Path
from django.core.mail import EmailMultiAlternatives
import os

class MailView(ViewSet):
    
    def all_mail(self, request):
        queryset = Mail.objects.filter(deleted_at__isnull=True)
        serializer = PostSerializer(queryset, many=True, not_fields=['created_at', 'updated_at', 'deleted_at'])
        return response_data(serializer.data)
    
    def get_mail_data(self, id):
        validate = IdGetMailValidate(data={'id':id})
        if not validate.is_valid():
            return False, validate.errors
        return True, validate.data['data']
    
    def add_mail(self, request):
        data = request.data.copy()
        mail_save = MailSerializer(data=data)
        if not mail_save.is_valid():
            return validate_error(mail_save.errors,STATUS['INPUT_INVALID'])
        mail_save.save()
        return response_data(mail_save.data)
    
    def edit_mail(self, request, id):
        data = request.data.copy()
        status, data_id = self.get_mail_data(id)
        if not status:
            return response_data(message=ERROR['not_exists_mail'],status=STATUS['NO_DATA'])
        queryset = Mail.objects.get(id=data_id['id'])
        data_save = MailSerializer(queryset, data=data, partial=True)
        if not data_save.is_valid():
            return validate_error(data_save.errors, STATUS['FAIL_REQUEST'])
        data_save.save()
        return response_data(data_save.data)
    
    def send_mail(self, request, id):
        data = request.data.copy()
        status, data_id = self.get_mail_data(id)
        if not status:
            return response_data(message=ERROR['not_exists_mail'],status=STATUS['NO_DATA'])
        mail = Mail.objects.get(id=data_id['id'])
        try:
            send_mail(
                subject=mail.title,
                message=mail.content,
                from_email=mail.from_mail,
                recipient_list=[mail.to],
                auth_user=mail.from_mail,
                auth_password=USER_SEND_MAIL['password_mail'],
                fail_silently = USER_SEND_MAIL['fail_silently'][0]
            )
        except:
            return response_data(message=ERROR['send_mail_faild'], status=STATUS['FAIL_REQUEST'])
        mail.status = 2
        mail.description = 'sucess'
        mail.save()
        return response_data(message=SUCCESS['send_mail'])
    
    def send(self, request):
        img_dir = 'api_app'
        image = 'test.png'
        file_path = os.path.join(img_dir, image)
        image_name = Path(file_path).name
        
        subject = 'Django sending email'
        body_html = f'''
            <html>
                <body>
                    <h1>abc</h1>
                    <img src="cid:{image_name}" />
                </body>
            </html>
        '''
        text_message = f"Email with a nice embedded image {image_name}."

        from_email = 'phuongnam.kimnt1@fpt.net'
        to_email = 'kimnguyen035171@gmail.com'

        msg = EmailMultiAlternatives(
            subject,
            text_message,
            from_email=from_email,
            to=[to_email]
        )

        msg.mixed_subtype = 'related'
        msg.attach_alternative(body_html, "text/html")
        
        with open(file_path, 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-ID', f'<{image_name}>'.format(name=image_name))
        msg.attach(img)
        msg.send()
        return response_data()