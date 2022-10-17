from django.shortcuts import render,  redirect
from datetime import datetime
from .models import Author, Comment
from .forms import CommentForm, AddContactViaModelForm
from django.contrib import messages
from .forms import  UserRegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def comments(request):
    all_comments = Comment.objects.all().order_by('-issued')

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = Author.objects.get(email=request.user.email)
            new_comment.issued = datetime.now()

            new_comment.save()
            form.save_m2m()

            return redirect('comments')

    return render(request, 'comments.html', {'comments':all_comments, 'form':form}) 

def add_model_comment(request):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            new_comment = form.save(commit=False)

            new_comment.author = Author.objects.get(email=request.user.email)

            new_comment.issued = datetime.now()

            new_comment.save()
            form.save_m2m()

            return redirect('comments')

    return render(request, 'add_comment.html', {'form':form})

def home(request):
    context = {}

    form = AddContactViaModelForm()

    error = ''

    if request.method == 'POST':
        form = AddContactViaModelForm(request.POST, request.FILES)

        if form.is_valid():
            new_contact = form.save(commit=False)

            new_contact.save()

            form.save_m2m()
 
            messages.success(request, 'Заявка успешно отправлена!')

            context = {'success'}
            return redirect('home')
        else:
            error = 'Форма была неверной'

    return render(request, 'home.html', {'form' : form,'error' : error, 'context': context}) 

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def services(request):
    return render(request, 'services.html')