from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserInformationForm
from .models import UserInformation

def user_info_form(request):
    """
    Renders the user information form and handles form submission.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered template response.
    """
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            # Check if a user with this username already exists in Django's User model
            if User.objects.filter(username=username).exists():
                error_message = 'User with this username already exists.'
                return render(request, 'error_page.html', {'error_message': error_message})
            
            # Check if a user with this email already exists in Django's User model
            if User.objects.filter(email=email).exists():
                error_message = 'User with this email already exists.'
                return render(request, 'error_page.html', {'error_message': error_message})
            
            # Create a Django User instance
            user = User.objects.create_user(
                username=username,
                email=email,
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )

            # Save specific fields from the form to the UserInformation model
            user_info = UserInformation.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                middle_initial=form.cleaned_data['middle_initial'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                zip_code=form.cleaned_data['zip_code'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                tagline=form.cleaned_data['tagline']
            )

            messages.success(request, 'User created successfully.')
            return redirect('confirmation_page')
    else:
        form = UserInformationForm()

    return render(request, 'user_info_form.html', {'form': form})

def confirmation_page(request):
    """
    Renders the confirmation page with the details of the last created user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered template response.
    """
    last_created_user = UserInformation.objects.last()
    return render(request, 'confirmation_page.html', {'user': last_created_user})
