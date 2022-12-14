KEY_RSA = 'duanfpro'

U = 'username'
P = 'password'

TOKEN = {
    'private_key':'anphMNcZkh',
    'public_key':'fnEcdMHkm',
    'type':'Bearer ',
    'hash':'HS256',
    'tls_access_token':60*60,
    'tls_refresh_token':60*60*3
}

GROUP_URL = {
    'url_auth',
}

THROTTLING = {
        'rate': '1',
        'split': '/',
        'per_time': '3s',
        'method': [
            'GET'
        ],
}

CELERY_QUEUE = {
    'retry_task': {
        'max_retries': 2,
        'countdown': 5
    }
}

USER_SEND_MAIL = {
    'from': 'phuongnam.kimnt1@fpt.net',
    'password_mail': 'K@12345abcd',
    'recipient_list': [
        'kimnguyen035171@gmail.com'
    ],
    'fail_silently': False,
    'connection': None,
    'html_message': None
}

SMTP_EMAIL = {
    'host': 'smtp.fpt.net',
    'port': 587,
    'host_user': 'phuongnam.kimnt1@fpt.net',
    'host_passwor': 'K@12345abcd',
    'use_tls': True,
    'use_ssl': False
}

JOB_SEND_MAIL = {
    'minute': '*/1',
    'hour': '*',
    'day': '*',
    'month': '*',
    'week': '*'
}

TIME_SEND_MAIL = ' '.join(JOB_SEND_MAIL.values())

CRON_JOB = {
    'cron_module': 'cron_jobs',
    'func_job_send_mail': 'send_mail_pnc',
    'scheduled_job_send_mail': TIME_SEND_MAIL
}