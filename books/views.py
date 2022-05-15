from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

from .models import Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    #get book comments
    book_comments = book.comments.all()

    context = {
        'book' : book,
        'comments' : book_comments,
    }
    return render(request, 'books/book_detail.html', context)

class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'description', 'price', 'book_cover']


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ['title', 'author', 'description', 'price', 'book_cover']


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

