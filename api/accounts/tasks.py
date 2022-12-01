from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from celery import shared_task


User = get_user_model()


@shared_task
def sender_token_verify_email(user_id, current_site):
    user = User.objects.get(pk=user_id)
    access_token = RefreshToken.for_user(user).access_token
    relativeLink = reverse('accounts:email-verify')
    absurl = 'http://' + current_site + relativeLink + "?token=" + str(access_token)
    email_body = 'Hi ' + user.username + \
                 ' Use the link below to verify your email \n' + absurl
    email = EmailMessage(
        f'Подтверждение адреса эллектронной почты',
        email_body,
        to=['djunpy@gmail.com'],
    )
    return email.send(fail_silently=False)
