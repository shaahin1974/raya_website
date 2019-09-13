from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from pages.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
                  path('', include('pages.urls')),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
                  path('djangoadmin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
