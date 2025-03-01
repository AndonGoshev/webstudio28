from django.urls import path

from webstudio28.common.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]