from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.views.author import AuthorViewSet

api_prefix = "api/v1"

router = DefaultRouter(trailing_slash=False)
router.register(r"authors", AuthorViewSet, basename="authors")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path(api_prefix + "/", include((router.urls, "bookshelf"), namespace="v1")),
]
