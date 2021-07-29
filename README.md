# DBlog
Blog page inspired by project publication 
Antonio Mele **"Django 3 By Example - Third Edition"**

# Source code for publication:
* [PacktPublishing - Django-3-by-Example](https://github.com/PacktPublishing/Django-3-by-Example)
  
# Important web resources
* [Official Django documentation - tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)

# Deployment guide

1) Create virtual environment for Python: **python -m venv venv**
2) Install Django with pip: ***pip install "Django==3.0.\*"***

# Testing

```
python manage.py shell
```
Write in shell:
```
>>> from django.contrib.auth.models import User
>>> from blog_app.models import Article
>>> user = User.objects.get(username='root')
>>> article = Article(title='Test article', slug='test', body='Text content', author=user)
>>> Article.objects.get(id='1')
>>> Article.objects.filter(publication_date__year=2021)
>>> Article.objects.order_by('title')
>>> Article.draft.filter(title__startswith='Test')
>>> article.delete()
```