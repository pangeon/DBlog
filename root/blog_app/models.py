from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    STATUS = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED')
    )
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=250, unique_for_date='publication_date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')

    class Meta:
        ordering = ('-publication_date',)

    def __str__(self):
        return self.title
