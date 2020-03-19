from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views import defaults as default_views


_urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    url(r'^_nested_admin/', include('nested_admin.urls')),
    url(r"^accounts/", include('django.contrib.auth.urls')),
]

_urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.

    _urlpatterns += [
        url(
            r"^400/$",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        url(
            r"^403/$",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        url(
            r"^404/$",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        url(r"^500/$", default_views.server_error)

    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        _urlpatterns += [
                           url(r"^__debug__/", include(debug_toolbar.urls))
        ]


urlpatterns = [
    url(r'^backend/', include(_urlpatterns))
]

admin.site.site_title = "HOME"
admin.site.site_header = "SUADE ADMINISTRATION"
