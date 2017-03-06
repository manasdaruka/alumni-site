from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit_profile/$',views.edit_profile,name='edit_profile'),
    url(r'^account_info/$', views.account_info, name='account_info'),
    url(r'^search/$', views.search, name='search'),
    url(r'^user/(?P<username>\w+)/$', views.public_profile, name='public_profile')
]