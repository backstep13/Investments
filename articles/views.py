from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article
from django.http import Http404


class Index(TemplateView):
    """Start page"""
    template_name = 'index.html'


class Contacts(TemplateView):
    "Page with contacts"
    template_name = 'contact-us.html'


class Calc(TemplateView):
    "Page with financial calculator with django.unicorn"
    template_name = 'calc.html'


def blog(request):
    myarticle = Article.objects.order_by('-pub_date')[:4]
    return render(request, 'blog.html', {'myarticle': myarticle})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')

    return render(request, 'blog-details.html', {'article': a})
