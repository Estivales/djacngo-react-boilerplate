from django.conf import settings
from django.conf.urls import include, url
from django.views.decorators.cache import cache_page
from base import views as base_views

urlpatterns = [
    url(r'^api/v1/accounts/', include(('account.urls', 'account'), namespace='account')),

    url(r'', cache_page(settings.PAGE_CACHE_SECONDS)(base_views.IndexView.as_view()), name='index'),
]
