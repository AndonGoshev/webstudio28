from django.urls import path

from webstudio28.common.views import HomeView, AboutView, PricingView, ContactsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]