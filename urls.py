from django.contrib import admin
from django.urls.conf import path
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='admin')),
    path('admin/', admin.site.urls)
]
