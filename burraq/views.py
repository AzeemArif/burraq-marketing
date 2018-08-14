from django.http import HttpResponse
from django.views.generic import TemplateView

from burraq.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect, render_to_response
from burraq.models import *


def index(request):
    return HttpResponse("Hello, world. Burraq Marketing.")


class indexView(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        gallery_folder = GalleryFolders.objects.all()
        gallery_data = GalleryImages.objects.all()
        args = {'gallery': gallery_data, 'folders': gallery_folder,'form': form}
        return render(request, self.template_name, args)

    def post(self, request, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            message = message +"\n" + "From :" +from_email
            try:
                send_mail(subject, message, 'azeem.esketchers@gmail.com', ['mazeemarif0@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, self.template_name)
            # return redirect('success')


# def successView(request):
#     return HttpResponse('Success! Thank you for your message.')

class successView(TemplateView):
    template_name = 'success.html'

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name)