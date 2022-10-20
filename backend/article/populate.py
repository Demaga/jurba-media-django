import os
import sys
import django
from django.conf import settings
from app import settings as app_settings

sys.path.append("/backend")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
# settings.configure(default_settings=app_settings, DEBUG=True)
django.setup()

import random

from django.contrib.auth.models import Group, User
from faker import Faker
from slugify import slugify

from article.models import Article, NewsArticle, Tag


faker = Faker("uk_UA")


def create_entities(N=10):
    """
    Populate multiple entities here
    """

    # create several editors that will publish articles
    users = []
    editor_group = Group.objects.get(name="Editor")
    for i in range(3):
        f_username = faker.name()
        f_password = faker.password(length=10)
        user = User.objects.create(username=f_username, password=f_password)
        user.groups.set([editor_group])
        users.append(user)

    tags = []
    for i in range(N):
        f_name = faker.word()
        f_bg_color = faker.color()
        f_text_color = faker.color()
        tag = Tag.objects.create(
            name=f_name, bg_color=f_bg_color, text_color=f_text_color
        )
        tags.append(tag)

    # creating N articles
    for i in range(N):
        f_title = faker.sentence(nb_words=7, variable_nb_words=True)
        f_subtitle = faker.sentence(nb_words=5, variable_nb_words=True)
        f_image = faker.image_url()
        f_promo = True if i == N else False
        f_promo_image = faker.image_url() if f_promo else None
        f_slug = slugify(f_title)
        f_published = True
        f_markdown_body = (
            f"# {faker.sentence(nb_words=10)}\n"
            f"## {faker.sentence(nb_words=10)}\n"
            f"![Image]({faker.image_url()})\n"
            f"{faker.sentence(nb_words=100)}"
        )

        f_author = random.choice(users)

        article = Article.objects.create(
            title=f_title,
            subtitle=f_subtitle,
            image=f_image,
            promo=f_promo,
            promo_image=f_promo_image,
            slug=f_slug,
            published=f_published,
            markdown_body=f_markdown_body,
            author=f_author,
        )

        f_tags = random.choices(tags, k=3)
        article.tags.set(f_tags)

    # finished
    print("Finished...{} entries populated.".format(N))


if __name__ == "__main__":

    print("Initializing... checking syntax...")
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
        print("Found parameter N = {}".format(N))
        # calling method for data population
        create_entities(N)
    else:
        print("No additional parameter provided, populating default no. of entries.")
        create_entities()
