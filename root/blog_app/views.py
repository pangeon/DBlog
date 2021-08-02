import about as about
import content as content
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Article


def _create_paginator(posts_on_site, collection):
    paginator = Paginator(collection, posts_on_site)
    return paginator


def show_articles(request):
    paginator = _create_paginator(3, Article.objects.all())
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(page.num_pages)

    return render(
        request,
        'articles_list.html',
        {
            'page': page,
            'articles': articles
        }
    )


def show_article_details(request, year, month, day, article):
    article = get_object_or_404(
        Article,
        slug=article,
        status='published',
        publication_date__year=year,
        publication_date__month=month,
        publication_date__day=day
    )
    return render(
        request,
        'article_details.html',
        {
            'article': article
        }
    )


class InfoView(View):
    def get(self, request):
        print(request.headers)
        return render(request, 'about.html', {
            'agent': request.headers['User-Agent'],
            'host': request.headers['Host']
        })
