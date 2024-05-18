import random
from django.conf import settings
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from django.contrib.sites.shortcuts import get_current_site

def send_generated_otp_to_email(email, request):
    # Generate and send an OTP to the user's email for verification
    subject = "One time passcode for Email verification"
    otp = random.randint(1000, 9999)  # Generate a random 4-digit OTP
    current_site = get_current_site(request).domain
    user = User.objects.get(email=email)
    email_body = f"Hi {user.first_name}, thanks for signing up on {current_site}. Please verify your email with the one-time passcode {otp}"
    from_email = settings.EMAIL_HOST
    otp_obj = OneTimePassword.objects.create(user=user, otp=otp)
    # Send the email
    d_email = EmailMessage(subject=subject, body=email_body, from_email=from_email, to=[user.email])
    d_email.send()

def send_normal_email(data):
    # Send a regular email based on the provided data
    email = EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email=settings.EMAIL_HOST_USER,
        to=[data['to_email']]
    )
    email.send()
