from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'publication_date', 'status')
    list_filter = ('status', 'created_date', 'publication_date', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publication_date'
    ordering = ('status', 'publication_date')
