from django.shortcuts import render, redirect
from django.contrib import messages
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
    # If form submitted
    if request.method == 'POST':
        # Validate form
        form = UserInformationForm(request.POST)
        if form.is_valid():
            # Check if user with this email already exists
            email = form.cleaned_data['email']
            if UserInformation.objects.filter(email=email).exists():
                error_message = 'User with this email already exists.'
                return render(request, 'error_page.html', {'error_message': error_message})
            else:
                # Save form
                form.save()
                messages.success(request, 'User created successfully.')
                return redirect('confirmation_page')
    else:
        # Render empty form
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