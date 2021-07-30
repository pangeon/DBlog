from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path(
        '',
        views.show_articles,
        name='articles_list'
    ),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:article>/',
        views.show_article_details,
        name='article_details'
    ),
]
