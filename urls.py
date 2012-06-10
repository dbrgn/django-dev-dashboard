from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$',                       'dashboard.views.index_explicit',   name="dashboard-index"),
    url('^all/$',                   'dashboard.views.index_all',        name="dashboard-index-all"),
    url('^metric/([\w-]+)/$',       'dashboard.views.metric_detail',    name="metric-detail"),
    url('^metric/([\w-]+).json$',   'dashboard.views.metric_json',      name="metric-json"),
    url(r'^admin/', include(admin.site.urls)),
)
