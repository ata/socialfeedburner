from django.contrib import admin
from socialauth.models import *

admin.site.register(UserProfile)
admin.site.register(FacebookUserProfile)
admin.site.register(TwitterUserProfile)
