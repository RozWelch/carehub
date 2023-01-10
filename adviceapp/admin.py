from django.contrib import admin
from .models import Carearticle, Article_comments
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Carearticle)
class CarearticleAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('article_title',)}
    list_filter = ('approved_status', 'created_on')
    list_display = ('article_title', 'slug', 'approved_status', 'created_on')
    search_fields = ['article_title', 'content']
    summernote_fields = ('content')

@admin.register(Article_comments)
class Article_commentsAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'article_comment', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
