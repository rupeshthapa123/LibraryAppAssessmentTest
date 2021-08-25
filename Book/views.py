from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import BookCreate
from .models import Book
from django.http import HttpResponse
from django.contrib import messages 
# Create your views here.

def index(request):
    shelf = Book.objects.all()
    return render(request, 'index.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            messages.success(request, "Book added Successfully")
            return redirect('/')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ / }}">reload</a>""")
    else:
        return render(request, 'book_upload.html', {'upload_form':upload})

def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('/')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('/')
    return render(request, 'book_upload.html', {'upload_form':book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('/')
    if book_sel.picture:
        book_sel.picture.delete()
    book_sel.delete()
    messages.error(request, "Book has been deleted Successfully")
    return redirect('/')
