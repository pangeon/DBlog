from django.shortcuts import render, get_object_or_404

from .models import Article


def show_articles(request):
    return render(
        request,
        'articles_list.html',
        {
            'articles': Article.published.all()
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
