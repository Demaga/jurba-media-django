from article.models import Article
from django.contrib import admin

# Register your models here.
from django.db import models
from martor.widgets import AdminMartorWidget


class ArtcicleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": AdminMartorWidget},
    }


admin.site.register(Article, ArtcicleAdmin)
