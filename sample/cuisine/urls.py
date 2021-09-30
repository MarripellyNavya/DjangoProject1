from django.conf.urls import url
from . import views

urlpatterns = [
 # Cuisine_list view as a function
    url(r'^$', views.CuisineListView.as_view(), name='cuisine_list_cls'),
    
 # Cuisine_detail view as a function
    url(r'^(?P<cuisine>[-\w]+)/$',
        views.Cuisine_detail,
        name='Cuisine_detail'
        ),
]

