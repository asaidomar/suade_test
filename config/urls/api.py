from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.shortcuts import redirect

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="API")


def home(request):
    return redirect(request._current_scheme_host.replace("api.", ""))


urlpatterns = [
    url(r'^ui/$', schema_view),
    url(r'^front/index.html', home),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] \
                      + urlpatterns
