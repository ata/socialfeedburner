from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from socialauth.models import UserProfile

def need_profile(f):
    @login_required
    def decorated(*args, **kwargs):
        try: 
            args[0].user.get_profile()
        except: 
            UserProfile(user=args[0].user).save()
            #return HttpResponseRedirect(reverse('socialauth_profile'))
        return f(*args, **kwargs)
    return decorated 
