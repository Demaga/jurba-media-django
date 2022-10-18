import tempfile

from article.models import Article
from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class ArticleTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.author = User.objects.create(username="Editor", password="Editor")
        cls.article = Article.objects.create(
            title="Testing title",
            subtitle="the title we deserved",
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            slug="testing-title",
            markdown_body="# Testing title\n## the title we deserved\nSome actual body text",
            author=cls.author,
        )

    def test_article_creation(self):
        """Check that article was successfully created"""
        article = Article.objects.get(slug="testing-title")
        self.assertEqual(article.title, "Testing title")
