from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, BlogPostForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after signup
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')  # Redirect to dashboard after login
            else:
                # Handle invalid login attempt
                print("Authentication failed")
        else:
            # Handle invalid form
            print("Form is not valid")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'dashboard.html')

def create_blog(request):
    if request.user.user_type != 'doctor':
        return redirect('dashboard')
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('dashboard')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog.html', {'form': form})
@login_required
def view_blogs(request):
    if request.user.user_type == 'doctor':
        blogs = BlogPost.objects.filter(author=request.user)
    else:
        blogs = BlogPost.objects.filter(is_draft=False)
    return render(request, 'view_blogs.html', {'blogs': blogs})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)

    # Check if the user is the author of the blog and is a doctor
    if blog.author == request.user and request.user.user_type == 'doctor':
        if request.method == 'POST':
            blog.delete()
            return redirect('view_blogs')  # Redirect to the list of blogs
    else:
        raise PermissionDenied
    
    return render(request, 'confirm_delete.html', {'blog': blog})

def logout_user(request):
    logout(request)
    return redirect('login')
