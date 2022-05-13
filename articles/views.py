from django.shortcuts import render
from .models import Article
from django.http import Http404


def blog(request):
    myarticle = Article.objects.order_by('-pub_date')[:4]
    return render(request, 'list.html', {'myarticle': myarticle})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена')

    return render(request, 'details.html', {'article': a})
