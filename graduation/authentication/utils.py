import random
from django.conf import settings
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from django.contrib.sites.shortcuts import get_current_site


def send_generated_otp_to_email(email, request): 
    subject = "One time passcode for Email verification"
    otp=random.randint(1000, 9999) 
    current_site=get_current_site(request).domain
    user = User.objects.get(email=email)
    email_body=f"Hi {user.first_name} thanks for signing up on {current_site} please verify your email with the \n one time passcode {otp}"
    from_email=settings.EMAIL_HOST
    otp_obj=OneTimePassword.objects.create(user=user, otp=otp)
    #send the email 
    d_email=EmailMessage(subject=subject, body=email_body, from_email=from_email, to=[user.email])
    d_email.send()


def send_normal_email(data):
    email=EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email=settings.EMAIL_HOST_USER,
        to=[data['to_email']]
    )
    email.send()


# def generateOtp():
#     otp=""
#     for i in range(6):
#         otp += str(random.randint(1, 9))
#     return otp


# def send_code_to_user(email):
#     Subject="One time passcode for Email verification"
#     otp_code=generateOtp()
#     print(otp_code)
#     user=User.objects.get(email=email)
#     current_site="myAuth.com"
#     email_body=f"Hi {user.username} thanks for signing up on {current_site} please verify your email with the \n on time passcode {otp_code}"
#     from_email=settings.DEFAULT_FROM_EMAIL

#     OneTimePassword.objects.create(user=user, code=otp_code)

#     send_email=EmailMessage(subject=Subject, body=email_body, from_email=from_email, to=[email])
#     send_email.send(fail_silently=True)


