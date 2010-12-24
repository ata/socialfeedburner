import os.path
from djangoappengine.settings_base import *

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'djangoappengine',
    'djangotoolbox',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'mediagenerator',
    # Apps
    'socialauth',
    'newsfeed',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'mediagenerator.middleware.MediaMiddleware',
    #'extras.middleware.CleanWhiteSpaceMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)


ADMIN_MEDIA_PREFIX = '/media/admin/'
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

# MY SETTING

# Auth
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

AUTH_PROFILE_MODULE = 'socialauth.UserProfile'


# MEDIA GENERATOR SETTING

MEDIA_DEV_MODE = DEBUG
DEV_MEDIA_URL = '/devmedia/'
PRODUCTION_MEDIA_URL = '/media/'

GLOBAL_MEDIA_DIRS = (os.path.join(os.path.dirname(__file__), 'media'),)

MEDIA_BUNDLES = (
    ('main.css',
        'css/screen.css',
        'css/main.css',
    ),
    ('print.css',
        'css/print.css'
    ),
    ('ie.css',
        'css/ie.css'
    ),
    ('main.js',
        'js/jquery-1.4.4.js',
        #'js/mootools-more-1.3.js',
        'js/main.js'
    ),
)

ROOT_MEDIA_FILTERS = {
    'js': 'mediagenerator.filters.yuicompressor.YUICompressor',
    'css': 'mediagenerator.filters.yuicompressor.YUICompressor',
}

YUICOMPRESSOR_PATH = os.path.join(os.path.dirname(__file__),
    'tools/yuicompressor.jar')

#END MEDIA GENERATOR SETTING


TIME_ZONE = 'Asia/Jakarta'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True
USE_L10N = True

CONSUMER_KEY = '6gFhpxXSeSi2OHGpAnWZw'
CONSUMER_SECRET = 'Wrz4sJrhHvZlrGUU6Djp85GWX0DuYM6q09gs42Gvq4'

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

# TWITTER SETTING
if DEBUG:
    TWITTER_CONSUMER_KEY = 'mSfl4UC4pQgILTqNWGaoA'
    TWITTER_CONSUMER_SECRET = 'Fls41aDyjt8T4Qqw3XS1Zsu58kpRJK7dp2fCeFUYBU'
else:
    TWITTER_CONSUMER_KEY = 'Jw1CVRMB6g0T4tqSzAPI4g'
    TWITTER_CONSUMER_SECRET = 'VM6OTzlhbyDsH11JiOZvS6689TnVUNHfwa9C8Bs7BM'



