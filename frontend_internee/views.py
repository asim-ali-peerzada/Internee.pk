from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CustomUserprofile

@login_required
def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        user = authenticate(username=username, password=password)
         
        if user is None:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
        else:
            login(request, user)
            return redirect('portal')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
         
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken!")
            return redirect('/signup')
         
        user = User.objects.create_user(
            username=username,
            email=email,
        )
         
        user.set_password(password)
        user.save()
         
        messages.info(request, "Account created successfully!")
        return redirect('login')
    return render(request, 'signup.html')


def portal(request):
    user = request.user
    user_profile, created = CustomUserprofile.objects.get_or_create(user=user)

    if request.method == 'POST':
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        skills = request.POST.get('skills')
        description = request.POST.get('description')
        profile_photo = request.FILES.get('profile_photo')

        if name:
            user.username = name
            user.save()

        user_profile.bio = bio
        user_profile.skills = skills
        user_profile.description = description
        if profile_photo:
            user_profile.profile_photo = profile_photo
        user_profile.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('portal')

    context = {
        'user': user,
        'user_profile': user_profile
    }
    return render(request, 'portal.html', context)


# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully.')
#             return redirect('portal')  # Redirect to profile page after saving
#     else:
#         form = ProfileUpdateForm(instance=request.user)
    
#     return render(request, 'portal.html', {'form': form})