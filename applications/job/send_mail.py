from django.core.mail import send_mail
from django.core.mail import send_mail
from config.celery import app

@app.task
def send_confirmation_email(email, code):
    full_link = f'Hello, please confirm that you really want this job offer \nTap this -> http://localhost:8000/api/v1/job/confirm/{code}'    
    send_mail(
        f'Job confirm',
        full_link,
        'dcabatar@gmail.com',
        [email]
    )
    
    
@app.task
def send_email_to_owner(email, carrier):
    full_link = f'Hello, {carrier} wants to take this job, please confirm it'
    send_mail(
        f'Job confirm',
        full_link,
        'dcabatar@gmail.com',
        [email]
    )
    