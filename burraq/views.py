from django.http import HttpResponse
from burraq.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Hello, world. Burraq Marketing.")


def indexView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['mazeemarif0@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "index.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')