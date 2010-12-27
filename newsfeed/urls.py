from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('newsfeed.views',
    url(r'^$', 'index', name='newsfeed'),    
    url(r'^firstload/?$', 'firstload', name='newsfeed_firstload'), 
    url(r'^newest/(?P<since_id>\d+)/?$','newest',name='newsfeed_newest'),
    url(r'^older/(?P<max_id>\d+)/?$','older',name='newsfeed_older'),
)
