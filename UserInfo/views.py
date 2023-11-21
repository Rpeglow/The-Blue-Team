from django.shortcuts import render
from .forms import UserInformationForm

def user_info_form(request):
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserInformationForm()

    return render(request, 'user_info_form.html', {'form': form})
