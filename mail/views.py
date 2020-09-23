from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):

    send_mail('teste de envio de emails com python e django',
    'Olha, esse é um teste de envio de emails com python e django',
    'gb.pydeveloper@gmail.com',
    ['gabrielchamex@gmail.com'],
    fail_silently = False)

    return render(request, 'mail/index.html')