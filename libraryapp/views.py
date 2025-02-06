from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from .models import Book
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def viewbooks(request):
    filter_option = request.GET.get('filter', 'all')

    if filter_option == 'not_borrowed':
        books = Book.objects.filter(is_borrowed=False)
    elif filter_option == 'not_available':
        books = Book.objects.filter(is_borrowed=True).exclude(borrowed_by=request.user)
    else:
        books = Book.objects.all()
    
    return render(request, 'libraryapp/viewbook.html', {'books': books, 'filter_option': filter_option})

def viewbookdetails(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'libraryapp/viewbookdetails.html', {'book': book})


def editbook(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        # Update book details from form data
        book.name = request.POST.get('bookName')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.category = request.POST.get('category')
        book.save()
        messages.success(request, 'Book details updated successfully!')
        return redirect('viewbooks')
    return render(request, 'libraryapp/editbook.html', {'book': book})


def delete_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(pk=book_id)
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('viewbooks')
    return HttpResponseNotAllowed(['POST'])

def borrow_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=book_id)
        book.is_borrowed = True
        book.borrowed_by = request.user 
        book.save()
        messages.success(request, "You have successfully borrowed the book.")
        return redirect('viewbooks')
    return HttpResponseNotAllowed(['POST'])

def return_book(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)

        if book.is_borrowed and book.borrowed_by == request.user:
            book.is_borrowed = False
            book.borrowed_by = None
            book.save()
            messages.success(request, "You have successfully returned the book.")
        else:
            if book.borrowed_by != request.user:
                messages.error(request, "You cannot return a book you did not borrow.")
        return redirect('viewbooks')
    return HttpResponseNotAllowed(['POST'])
