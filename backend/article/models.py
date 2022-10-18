from app.models import Timestampable
from django.contrib.auth.models import User
from django.db import models
from martor.models import MartorField


# Create your models here.
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


class NewsArticle(Timestampable):
    title = models.CharField(max_length=150)
    image = models.ImageField(
        max_length=150, upload_to="./news_articles", null=True, blank=True
    )
    source = models.URLField()
    source_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
