from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Cuisine_list view as a function
def Product_list(request):
    """function to implement the logic of the list view for Cuisine"""
    object_list = Product.objects.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        mobiles = paginator.page(page)
    except PageNotAnInteger: # If page is not an integer deliver the first page
        mobiles = paginator.page(1)
    except EmptyPage: # If page is out of range deliver last page of results
        mobiles = paginator.page(paginator.num_pages)
    return render(request,'mobile/mobile/list.html',{'page': page, 'mobiles': mobiles})
# -------------------------------------------------------------
# Cuisine_detail view as a function
def Product_detail(request, mobile):
    """function to implement the logic of the detail view for Cuisine"""
    mobileClicked = get_object_or_404(
    Product,
    slug=mobile,
    status='published'
    )
    return render(request,'mobile/mobile/detail.html',{'mobile': mobileClicked})
