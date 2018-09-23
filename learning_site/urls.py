from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'learning_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', views.hello_world),
    url(r'^courses/', include('courses.urls',namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),

]
