from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls import include
 
urlpatterns = [
    path('', views.index_template, name='index'),
    path('index.html/', views.index_template, name='index'),
    path('access.html/', views.access_template, name='access'),
    path('menu.html/', views.menu_template, name='menu'),
    path('works.html/', views.works_template, name='works'),
    path('staff.html/', views.staff_template, name='staff'),
    path('shop.html/', views.shop_template, name='shop'),
    path('link.html/', views.link_template, name='link'),
    path('boxbox.html/', views.boxbox_template, name='boxbox'),
    path('contact.html/', views.contact_template, name='contact'),
    path('recruit.html/', views.recruit_template, name='recruit'),
    path('sitemap.html/', views.sitemap_template, name='sitemap'),
]

