from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserInformationForm
from .models import UserInformation

def user_info_form(request):
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if UserInformation.objects.filter(email=email).exists():
                error_message = 'User with this email already exists.'
                return render(request, 'error_page.html', {'error_message': error_message})
            else:
                form.save()
                messages.success(request, 'User created successfully.')
                return redirect('confirmation_page')
    else:
        form = UserInformationForm()

    return render(request, 'user_info_form.html', {'form': form})

def confirmation_page(request):
    last_created_user = UserInformation.objects.last()
    return render(request, 'confirmation_page.html', {'user': last_created_user})