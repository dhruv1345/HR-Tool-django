from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import TrackedFile, Version
from .forms import UploadFileForm, FileEditForm

def home(request):
    return render(request, 'tracker/home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created!")
        return redirect('login')

    return render(request, 'tracker/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('file_list')

        messages.error(request, "Invalid credentials")

    return render(request, 'tracker/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def upload_file(request):
    if request.method == 'POST':
        name = request.POST['name']
        content = request.POST['content']
        uploaded_file = request.FILES.get('uploaded_file')  # ✅ get uploaded file

        file = TrackedFile.objects.create(
            name=name,
            current_content=content,
            uploaded_file=uploaded_file,  # ✅ save uploaded file
            uploaded_by=request.user
        )

        Version.objects.create(
            file=file,
            editor=request.user,
            content=content
        )

        return redirect('file_list')

    return render(request, 'tracker/upload.html')

@login_required
def file_list(request):
    files = TrackedFile.objects.all()
    return render(request, 'tracker/file_list.html', {'files': files})

@login_required
def edit_file(request, file_id):
    file = get_object_or_404(TrackedFile, pk=file_id, uploaded_by=request.user)
    
    if request.method == 'POST':
        form = FileEditForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileEditForm(instance=file)

    return render(request, 'tracker/edit_file.html', {'form': form, 'file': file})


@login_required
def file_history(request, file_id):
    file = get_object_or_404(TrackedFile, id=file_id)
    versions = file.versions.order_by('-edited_at')
    return render(request, 'tracker/history.html', {'file': file, 'versions': versions})

