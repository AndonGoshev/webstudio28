from django.urls import path

from django.contrib.sitemaps.views import sitemap
from webstudio28.common.sitemaps import StaticViewSitemap

from webstudio28 import settings
from webstudio28.common.views import HomeView, AboutView, PricingView, ContactsView, MessageSentSuccessfullyView

from django.views.static import serve


sitemaps = {
    'static': StaticViewSitemap
}
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('contacts/message-sent-successfully/', MessageSentSuccessfullyView.as_view(),
         name='message-sent-successfully'),
    path("robots.txt", serve, {"path": "robots.txt", "document_root": settings.STATIC_URL}),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
