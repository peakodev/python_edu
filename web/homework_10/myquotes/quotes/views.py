from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from quotes.models import Author, Quote
from quotes.forms import AuthorForm, QuoteForm


def index(request: HttpRequest):
    quotes = Quote.objects.order_by('-pab_date')
    paginator = Paginator(quotes, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'quotes/quotes.html', {'page_obj': page_obj})


def author_detail(request: HttpRequest, author_slug):
    author = get_object_or_404(Author, slug=author_slug)
    return render(request, 'quotes/author_detail.html', {'author': author})


def quotes_by_tag(request: HttpRequest, tag):
    quotes = [quote for quote in Quote.objects.all() if tag in quote.tags]
    paginator = Paginator(quotes, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'quotes/quotes.html', {'page_obj': page_obj, 'tag': tag})


@login_required
def author(request: HttpRequest):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()

            return redirect(to='quotes:author_detail', author_slug=author.slug)
        else:
            return render(request, 'quotes/author.html', {'form': form})

    return render(request, 'quotes/author.html', {'form': AuthorForm()})


@login_required
def quote(request):
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            author = Author.objects.get(id=request.POST.get('author'))
            new_quote.user = request.user
            new_quote.author = author
            new_quote.save()

            return redirect(to='quotes:index')
        else:
            return render(request, 'quotes/quote.html', {"authors": authors, 'form': form})

    return render(request, 'quotes/quote.html', {"authors": authors, 'form': QuoteForm()})
