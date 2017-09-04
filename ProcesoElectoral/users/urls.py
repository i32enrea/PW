from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^login$', views.login_user.as_view(), name = 'login'),
                       url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page':'home'}, name = 'logout'),
                       )