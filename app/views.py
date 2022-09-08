from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
 
def home(request):

    send_mail('Hey, sending from beejaxx',
    'HI, this mail is  coming from beejaxx',
    'beejaxxtech@gmail.com',
    ['rakimad436@pelung.com', 'beejaxx17@gmail.com'],
    fail_silently=False)
    return render(request, 'home.html')