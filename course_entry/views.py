from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Image

# Create your views here.
def course_list(request):
    return render(request, 'course_entry/course_list.html', {})

def image_page(request):
    images = Image.objects.all()
    return render(request, 'course_entry/image_page.html', {'images': images})

def image_detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    
    app_name = image.page
    
    app_url = f'/{app_name}/'
    
    return redirect(app_url)

def about(request):
    return render(request, 'course_entry/about.html', {})

def FAQ(request):
    return render(request, 'course_entry/FAQ.html', {})


def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)

def success_page(request):
    return render(request, 'course_entry/success.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('success_page')
    else:
        form = AuthenticationForm()
    return render(request, 'course_entry/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'course_entry/logout.html')