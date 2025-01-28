from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from posts.models import Post


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                return redirect('login')
            
    form = LoginForm()
    return render(request, 'login.html', {'form':form} )

@login_required
def user_post(request):
    current_user = request.user
    posts = Post.objects.filter(user=current_user)
    return render(request, 'index.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST) 
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('register_complete')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def register_compelete(request):
    return render(request, 'register_complete.html')


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})



@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        user_from = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_from.is_valid() and profile_form.is_valid():
            user_from.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_from = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'user_form': user_from, 'profile_form': profile_form})

