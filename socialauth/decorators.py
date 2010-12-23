from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def need_profile(f):
    @login_required
    def decorated(*args, **kwargs):
        try: 
            args[0].user.get_profile()
        except: 
            return HttpResponseRedirect(reverse('socialauth_profile'))
        return f(*args, **kwargs)
    return decorated 

def needs_user(url):
    def decorated1(f):
        @wants_user
        def decorated2(*args, **kwargs):
            if not args[0].user: 
                return HttpResponseRedirect(reverse(url))
            else: 
                return f(*args, **kwargs)
        return decorated2
    return decorated1
