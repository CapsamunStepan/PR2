from django.shortcuts import render
from .forms import GmailMessageForm, GmailInboxForm
from django.core.mail import send_mail
from .get_messages import read_emails
import time


# Create your views here.
def home_view(request):
    return render(request, 'lab2/home.html')


def send_message(request):
    sent = False
    if request.method == 'POST':
        form = GmailMessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            sender_email = cd.get('sender_email')
            recipient_email = cd.get('recipient_email')
            subject = cd.get('subject')
            message = cd.get('message')
            password = cd.get('sender_password')
            send_mail(subject=subject,
                      message=message,
                      from_email=sender_email,
                      recipient_list=[recipient_email],
                      auth_user=sender_email,
                      auth_password=password)
            sent = True
    else:
        form = GmailMessageForm()
    return render(request, 'lab2/send.html', {'form': form, 'sent': sent})


def view_messages(request):
    get = False
    messages = {}
    if request.method == 'POST':
        form = GmailInboxForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd.get('email')
            password = cd.get('password')
            messages = read_emails(email, password)
            messages = dict(reversed(list(messages.items())))
            # time.sleep(1)
            get = True
    else:
        form = GmailInboxForm()

    return render(request, 'lab2/get.html', {'form': form, 'messages': messages, 'get': get})
