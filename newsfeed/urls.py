from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('newsfeed.views',
    url(r'^$', 'index', name='newsfeed'),    
    url(r'^newest$','newest',name='newsfeed_newest'),
)
