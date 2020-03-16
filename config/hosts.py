from django.conf import settings
from django_hosts import patterns, host

sub_domains = (
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'api', 'config.urls.api', name='api')
)

host_patterns = patterns('', *sub_domains)
