from article.models import Article, NewsArticle
from article.serializers import ArticleSerializer, NewsArticleSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """

    queryset = Article.objects.all().order_by("-created_at")
    serializer_class = ArticleSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False)
    def published_articles(self, request):
        articles = Article.objects.filter(published=True).order_by("-created_at")

        # page = self.paginate_queryset(recent_users)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data)


class NewsArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows news articles to be viewed or edited.
    """

    queryset = NewsArticle.objects.all().order_by("-created_at")
    serializer_class = NewsArticleSerializer
    # permission_classes = [permissions.IsAuthenticated]
