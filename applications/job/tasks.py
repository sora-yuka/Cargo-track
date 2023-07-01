from django.core.mail import send_mail
from django.core.mail import send_mail
from config.celery import app

@app.task
def send_confirmation_email(email, code, code2):
    full_link = f'Hello, please confirm that you really want this job offer \nTap this -> https://web.whatsapp.com/ \n  http://localhost:8000/api/v1/job/confirm/{code} \n http://localhost:8000/api/v1/job/cancel/{code2}'    
    send_mail(
        f'Job confirm',
        full_link,
        'dcabatar@gmail.com',
        [email]
    )
    
    
@app.task
def send_email_to_owner(email, carrier):
    full_link = f'Hello, {carrier} wants to take this job, please confirm it. Tap this -> '
    send_mail(
        f'Job confirm',
        full_link,
        'dcabatar@gmail.com',
        [email]
    )
    