#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from libraryapp.models import Book

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                if user.is_staff:
                    messages.success(request, "Admin login successful!")
                    return redirect('viewbooks')
                else:
                    messages.success(request, "Login successful!")
                    return redirect('viewbooks')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Username and password are required")
    
    return render(request, 'libraryapp/login.html')

def user_logout(request):
    request.session.flush()

    if request.user.is_authenticated:
        Session.objects.filter(session_key=request.session.session_key).delete()
        auth_logout(request)
    
    return redirect('login')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        is_admin = request.POST.get('is_admin') == 'on'
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'libraryapp/signup.html')
        
        if len(password) <= 5:
            messages.error(request, "Password has to be more than 5 characters")
            return render(request, 'libraryapp/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'libraryapp/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'libraryapp/signup.html')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.is_staff = is_admin
        user.save()

        messages.success(request, "Registration successful!")
        return redirect('login')
    
    return render(request, 'libraryapp/signup.html')




def homepage(request):
  return render(request, 'index.html')

@login_required
def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        description = request.POST.get('description')
        category = request.POST.get('category')
        cover = request.FILES.get('cover')
        
        new_book = Book(
            name=name,
            author=author,
            description=description,
            category=category,
            cover=cover
        )
        new_book.save()
        
        messages.success(request, 'Book added successfully!')
        return redirect('viewbooks')
        
    return render(request, 'libraryapp/addbook.html')


@login_required
def borrowed_books(request):
    borrowed_books = Book.objects.filter(is_borrowed=True, borrowed_by=request.user)
    return render(request, 'libraryapp/borrowed.html', {'borrowed_books': borrowed_books})

@login_required
def search_books(request):
    search_query = request.GET.get('search_query', '').lower().strip()
    search_filter = request.GET.get('search_filter', '')

    if search_query:
        if search_filter == 'title':
            books = Book.objects.filter(name__icontains=search_query)
        elif search_filter == 'author':
            books = Book.objects.filter(author__icontains=search_query)
        elif search_filter == 'category':
            books = Book.objects.filter(category__icontains=search_query)
        else:
            books = Book.objects.filter(
                name__icontains=search_query,
                author__icontains=search_query,
                category__icontains=search_query
            )

    else:
        books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'libraryapp/search.html', context)