from app.models import Timestampable
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.db import models
from martor.models import MartorField


class Tag(models.Model):
    name = models.CharField(max_length=10)
    bg_color = ColorField(default="#1e488f")
    text_color = ColorField(default="#FFFFFF")

    def __str__(self):
        return self.name


class Article(Timestampable):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    image = models.ImageField(max_length=150, upload_to="./articles")
    promo = models.BooleanField(default=False)
    promo_image = models.ImageField(
        max_length=150, null=True, blank=True, upload_to="./articles"
    )
    slug = models.SlugField(max_length=150, unique=True)
    published = models.BooleanField(default=False)
    markdown_body = MartorField()

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)


class NewsArticle(Timestampable):
    title = models.CharField(max_length=150)
    image = models.ImageField(
        max_length=150, upload_to="./news_articles", null=True, blank=True
    )
    source = models.URLField()
    source_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
