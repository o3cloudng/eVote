from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from account.views import userlogin

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path('', userlogin, name="login"),
] + debug_toolbar_urls()


if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
    # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
