from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Contact


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name=name, last_name=last_name,
                          email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, 'ممنون از تماس شما')
        return render(request, 'contacts/contact_us.html')
    else:
        return render(request, 'contacts/contact_us.html')
