from django.core.mail import send_mail
from config.celery import app
from decouple import config


@app.task
def send_activation_code(user_email, code):
    link = f"http://{config('SERVER_IP')}/api/v1/account/confirm/{code}"
    send_mail(
        "Verification letter",
        f"Follow the link to activate account: {link}",
        config("EMAIL_HOST_USER"),
        [user_email]
    )