Install
    pip install django-crontab
Add django_crontab to INSTALLED_APPS
    INSTALLED_APPS = [
        'django_crontab',
        ...
    ]
Create a file cron job myapp/cron.py
    def my_cron_job():
    # your functionality goes here
Settings.py file
    CRONJOBS = [('*/2 * * * *', 'myapp.cron.my_cron_job')]
Add CRONJOBS to crontab
    python3 manage.py crontab add
Show all CRONJOBS
    python3 manage.py crontab show
Remove all CRONJOBS
    python3 manage.py crontab remove