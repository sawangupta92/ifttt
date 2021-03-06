from django.conf.urls  import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ifttt.views.home', name='home'),
    # url(r'^ifttt/', include('ifttt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^check_index','check.views.index'),
    url(r'^view_temp','check.views.view_temp'),
    url(r'^mail','check.views.mail'),
    url(r'^test','check.views.test'),
    url(r'^create_user','check.views.create_user'),
    url(r'^mysave','check.views.mysave')
)
