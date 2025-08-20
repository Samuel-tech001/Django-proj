from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Django homepage!")
from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    send_mail(
        subject='Test Subject',
        message='Test message body.',
        from_email='gitongasamuel814@gmail.com',
        recipient_list=['blackman011662@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("Email sent successfully!")