from django.urls import include, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from django_orghierarchy.api import OrganizationViewSet

router = DefaultRouter()
router.register(r"organization", OrganizationViewSet, "organization")

urlpatterns = [
    path(r"admin/", admin.site.urls),
    path(r"api/", include((router.urls, "api"), namespace="api")),
]
