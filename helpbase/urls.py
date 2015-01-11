from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import HomeView
from ticket.views import TicketCreateView


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^tickets/create', TicketCreateView.as_view()),
)
