from django.urls import path

from webstudio28.common.views import HomeView, AboutView, PricingView, ContactsView, MessageSentSuccessfullyView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('pricing/', PricingView.as_view(), name='pricing'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('contacts/message-sent-successfully/', MessageSentSuccessfullyView.as_view(), name='message-sent-successfully'),
]