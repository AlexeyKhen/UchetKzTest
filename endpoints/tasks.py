from celery import shared_task
from django.core.mail import send_mail


@shared_task
def sending_mail(mail, done):
    if done:
        message = 'You marked your task as completed'
    message = 'You marked your task as uncompleted'
    send_mail(
        'You changed your task',
        message,
        'alexey.khen@gmail.com',
        [mail])
    print(f'mail was sent {mail}')
    return None
