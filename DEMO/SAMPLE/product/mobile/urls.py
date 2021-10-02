from django.conf.urls import url
from . import views
urlpatterns = [
    
    url(r'^$',
        views.Product_list,
        name='Product_list' ),
    
    url(r'^(?P<mobile>[-\w]+)/$',
        views.Product_detail,
        name='Product_detail'
        ),
    ]
