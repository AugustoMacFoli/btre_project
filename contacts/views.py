from django.shortcuts import redirect
from django.contrib import messages
from .models import Contact
# from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
#        realtor_email = request.POST['realtor_email']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listings_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You already made a request. Please wait for our realtor to reply.')
                return redirect('/listings/' + listing_id)
        contact = Contact(listings=listing, listings_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
#        send_mail('Subject here',
#                  'Here is the message.',
#                  'admin@btrealestate.com',
#                  [realtor_email, email],
#                  fail_silently=False,)
        messages.success(request, 'Your request have been submitted, a realtor will get back to you soon.')
        return redirect('/listings/' + listing_id)