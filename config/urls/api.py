from django.conf import settings
from django.conf.urls import include, url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

swagger_info = openapi.Info(
    title="API DOCUMENTATION",
    default_version='v1',
    description="API DOCUMENTATION",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="saidomarali@gmail.com"),
    license=openapi.License(name="BSD License"),
)

schema_view = get_schema_view(
    swagger_info,
    validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),

    url(r'^cached/swagger(?P<format>.json|.yaml)$',
        schema_view.without_ui(cache_timeout=None),
        name='cschema-json'),
    url(r'^cached/swagger/$',
        schema_view.with_ui('swagger', cache_timeout=None),
        name='cschema-swagger-ui'),
    url(r'^cached/redoc/$',
        schema_view.with_ui('redoc', cache_timeout=None),
        name='cschema-redoc'),

    url(r'^rest/', include('core.vendors.urls')),
    url(r'^rest/', include('core.members.urls')),
    url(r'^rest/', include('core.products.urls')),
    url(r'^rest/', include('core.orders.urls')),
    url(r'^rest/', include('core.promotions.urls')),
]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] \
                      + urlpatterns
