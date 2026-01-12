from django.shortcuts import render
from category.models import Category


# Create your views here.

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

    # context = {
    #     "menu_links": menu_links,
    # }

    # return render(request, "store/store.html", context)