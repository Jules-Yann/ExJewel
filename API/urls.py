from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^store_one/$', views.store_one),
    url(r'^store_all/$', views.store_all),

    url(r'^get_item/$', views.get_item),
    url(r'^get_all_item/$', views.get_all_item),

    url(r'^delete/', views.delete),
    #url(r'^search/$', views.search)
]
