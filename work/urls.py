from django.conf.urls import url
from django.urls import path
from . import views
from django.views.static import serve 
from working import settings



urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('',views.homepageview ,name="index"),
    path('register/',views.usercreationview, name="register"),
    path('login/',views.login_me,name='login'),
    #path('show_profile/<username>',views.show_profile,name="show_profile"),
    path('logout/',views.logout_me,name='logout'),
    #url(r'^profile/(?P<username>[\w|\W.-]+)/$',views.profile),
    path('profile/<username>',views.profile,name="profile"),
    path('addbook',views.addBook,name ="addbook"),
    path('products',views.productshow, name="products"),
    path('userprofile',views.gotoprofile,name="userprofile"),
    path('detailsofbook/<bookid>',views.detailsofbook,name="detailsofbook"),
    path('requestBook/',views.requestabook,name="requestBook"),
    path('deletebook/<bookid>',views.deletebook,name="deletebook"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('online/',views.online,name="online")
    #path('search/',views.search,name="search"),
    #url(r'^requestabook/(?P<username>[\w|\W.-]+)/(?P<bookid>[\w|\W.-]+)/$',views.profile),
]
