from django.shortcuts import render, get_object_or_404
from .models import Cuisine
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

class CuisineListView(ListView):
 queryset = Cuisine.objects.all()
 context_object_name = 'cuisines'
 paginate_by = 3
 template_name = 'cuisine/cuisine/list.html'

# Cuisine_list view as a function
def Cuisine_list(request):
    """function to implement the logic of the list view for Cuisine"""
    object_list = Cuisine.objects.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        cuisines = paginator.page(page)
    except PageNotAnInteger: # If page is not an integer deliver the first page
        cuisines = paginator.page(1)
    except EmptyPage: # If page is out of range deliver last page of results
        cuisines = paginator.page(paginator.num_pages)
    return render(
        request,
        'cuisine/cuisine/list.html',
        {'page': page, 'cuisines': cuisines}
        )


#---------------------------------------------------------------
def Cuisine_detail(request, cuisine):
    """function to implement the logic of the detail view for Cuisine"""
    cuisineClicked = get_object_or_404(
    Cuisine,
    slug=cuisine,
    status='published'
    )
    return render(request,'cuisine/cuisine/detail.html',{'cuisine': cuisineClicked})

