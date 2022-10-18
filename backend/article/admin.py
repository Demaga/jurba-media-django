from article.models import Article
from django.contrib import admin

# Register your models here.
from django.db import models
from django.utils.html import format_html
from martor.widgets import AdminMartorWidget


class ArtcicleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "subtitle",
        "thumbnail",
        "author",
        "created_at",
        "published",
    )

    list_filter = (
        "author",
        "published",
    )

    autocomplete_fields = ("author",)

    formfield_overrides = {
        models.TextField: {"widget": AdminMartorWidget},
    }

    def thumbnail(self, obj):
        width, height = 150, 200
        html = '<img src="{url}" width="{width}" height={height} />'
        return format_html(html.format(url=obj.image.url, width=width, height=height))


admin.site.register(Article, ArtcicleAdmin)
