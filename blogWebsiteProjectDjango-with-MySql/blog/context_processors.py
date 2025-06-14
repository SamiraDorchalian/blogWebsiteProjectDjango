from django.utils.translation import gettext as _

def add_variable_to_context(request):
    return {
        'home': _('Home'),
        'blog': _('Blog'),
        'new_post': _('New Post'),
        'Welcome': _('Welcome'),
        'logout': _('logout'),
        'login': _('login'),
        'signup': _('signup'),
        'linkedin': _('LinkedIn'),
        'WelcometoPythonandDjangoBlog': _('Welcome to Python and Django Blog'),
        'Wesharepythonanddjangotipsandtrickshere': _('We share python and django tips and tricks here'),
    }