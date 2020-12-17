from django.contrib import admin
from django.urls.conf import include, path
from django.views.generic.base import RedirectView


urlpatterns = [
    # Home-Redirected URLs
    path('', RedirectView.as_view(url='admin')),

    # Admin URLS
    path('admin/', admin.site.urls),

    # Query Profiling URLs
    path('silk/', include('silk.urls', namespace='silk'))
]
