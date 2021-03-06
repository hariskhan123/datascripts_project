from django.shortcuts import render, redirect
from django.contrib import messages,admin
from django.core.mail import send_mail
from .models import ContactForm

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = ContactForm(name=name, email=email, phone=phone, subject=subject, message=message,)

        ContactForm.save()

        # Send Email
        send_mail(
            'Data Scripts Inquiry',
            'There has been an inquiry from ' + name + '. Sign into admin panel for more info',
            'hariswork123@gmail.com',
            ['datascripts@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, We will get back to you')
        return redirect('/index#contact')
