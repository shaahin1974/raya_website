from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['index', 'about', 'team']

    def location(self, item):
        return reverse(item)
