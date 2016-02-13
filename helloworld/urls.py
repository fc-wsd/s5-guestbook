from django.conf.urls import url
from django.contrib import admin

from gb import views as gb_views

urlpatterns = [
    url(r'^guestbook/([0-9]+)/$', gb_views.view_post),
    url(r'^guestbook/new/$', gb_views.new_post),
    url(r'^admin/', admin.site.urls),
]
