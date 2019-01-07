from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        context = {
            'values': request.POST
        }
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            messages.error(request, 'Password do not match.')
            return render(request, 'accounts/register.html', context)
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'accounts/register.html', context)
        if User.objects.filter(email=email).exists():
            messages.error(request, 'This e-mail is being used.')
            return render(request, 'accounts/register.html', context)
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        auth.login(request, user)
        messages.success(request, 'You are now logged in.')
        return redirect('index')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials.')
            context = {
                'username': username
            }
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out.')
        return redirect('index')