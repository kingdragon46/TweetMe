# -*- encoding: utf-8 -*-


from django.contrib import admin
from django.urls import path, include  # add this
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("tweets/", include("tweets.urls")), # Auth routes - login / register
    path("auth/", include("Authentication.urls")), # Auth routes - login / register
    # path("", include("app.urls"))             # UI Kits Html files
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)