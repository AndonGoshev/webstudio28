from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['home', 'about', 'pricing', 'contacts', 'message-sent-successfully']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == 'message-sent-successfully':
            return 0.2
        return 0.8
