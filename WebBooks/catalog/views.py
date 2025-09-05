from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, BookInstance, Author
from django.views.generic import ListView, DetailView


def index(request):
    text_head = 'у нас большой выбор книг, у Читай-города меньше'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available =\
        BookInstance.objects.filter(status__exact=3).count()
    author = Author.objects
    num_author = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'text_head': text_head,
               'books': books, 'num_books':num_books,
               'num_instance': num_instance,
               'num_instance_available': num_instance_available,
               'author': author, 'num_author': num_author,
               'num_visits': num_visits}
    return render(request, 'catalog/index.html', context)

class BookListView(ListView):
    model = Book
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

class AuthorListView(ListView):
    model=Author
    paginate_by = 4
class AuthorDetailView(DetailView):
    model = Author

from django.shortcuts import render

def about(request):
    text_head = 'О нашем книжном магазине'
    company_name = 'Книжный магазин'
    description = 'Мы - книжный магазин с богатой историей и огромным выбором книг на любой вкус.  Наша миссия - сделать чтение доступным каждому.'
    slide1_text = 'Классическая литература'
    slide2_text = 'Современная проза'
    slide3_text = 'Детская литература'
    slide4_text = 'Учебная литература'
    context = {
        'text_head': text_head,
        'company_name': company_name,
        'description': description,
        'slide1_text': slide1_text,
        'slide2_text': slide2_text,
        'slide3_text': slide3_text,
        'slide4_text': slide4_text,
    }
    return render(request, 'catalog/about.html', context)

def contact(request):
    text_head = 'Контакты'
    name = 'ООО "Интеллектуальные информационные системы"'
    address = 'Москва, ул. Планерная, д. 20, к. 1'
    tel = '495-345-45-45'
    email = 'iis.info@mail.ru'
    context = {
        'text_head': text_head,
        'name': name,
        'address': address,
        'tel': tel,
        'email': email,
    }
    return render(request, 'catalog/contact.html', context)
