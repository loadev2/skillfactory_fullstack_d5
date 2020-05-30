from django.shortcuts import render, redirect
from app_first.models import Book, Publisher
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def publisher_list(request):
    template = loader.get_template('publishers.html')
    publishers = Publisher.objects.all()
    publishers_list = []
    for publisher_item in publishers:
        books = Book.objects.filter(publisher = publisher_item)
        publishers_list.append({
            "ptitle" : publisher_item.title,
            "books" : books,
        })
    publishers_data = {
        "title": "Publishing houses",
        "publishers": publishers_list
    }
    return HttpResponse(template.render(publishers_data, request))



def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')