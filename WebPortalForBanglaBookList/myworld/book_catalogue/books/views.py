from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Books
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os

def books(req):
    # allbooks = Books.objects.values()
    # #template = loader.get_template('all_books.html')
    # #template = loader.get_template('test_table.html')
    # template = loader.get_template('w33_search_table.html')
    # context = {
    #     'allbooks' : allbooks
    # }
    # return HttpResponse(template.render(context,req))
    # #return HttpResponse(template.render())
    # #return HttpResponse('opop vivo'+str(req))
    template = loader.get_template('w33_search_table.html')
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    book_list = Books.objects.all()
    page = req.GET.get('page', 1)

    paginator = Paginator(book_list, 2)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    
    context = {
        'allbooks' : books,
        'pagenumber' : page,
        'base_dir' : base_dir
    }
    
    #return render(req, 'core/user_list.html', { 'users': users })
    #return render(req, 'templates/w33_search_table.html', { 'books': books })
    return HttpResponse(template.render(context,req))

# Create your views here.
