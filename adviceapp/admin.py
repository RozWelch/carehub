from django.contrib import admin
from .models import Carearticle
from django_summernote import SummernoteModelAdmin

@admin.register(Carearticle)
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = (articel_content)
