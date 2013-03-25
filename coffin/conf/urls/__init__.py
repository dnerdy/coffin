try:
    # Django >= 1.5
    from django.conf.urls import *
except ImportError:
    from django.conf.urls.defaults import *

handler404 = 'coffin.views.defaults.page_not_found'
handler500 = 'coffin.views.defaults.server_error'