from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm, FeedbackForm
from django.core.mail import send_mail
from django.conf import settings

def contact_list(request):
    contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Send feedback email to admin
            subject = 'Feedback from Contact Book'
            message = f"From: {form.cleaned_data['email']}\n\n{form.cleaned_data['message']}"
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],  # Send to admin email
                fail_silently=False,
            )
            return render(request, 'contacts/feedback_success.html')
    else:
        form = FeedbackForm()
    return render(request, 'contacts/feedback.html', {'form': form})
