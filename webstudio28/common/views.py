from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'common/home/home.html'


class AboutView(TemplateView):
    template_name = 'common/about/about.html'


class PricingView(TemplateView):
    template_name = 'common/pricing/pricing.html'


class ContactsView(TemplateView):
    template_name = 'common/contacts/contacts.html'


class MessageSentSuccessfullyView(TemplateView):
    template_name = 'common/contacts/message-sent.html'