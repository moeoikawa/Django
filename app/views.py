from django.shortcuts import render
from django.http.response import HttpResponse

def index_template(request):
    return render(request, 'index.html')

def access_template(request):
    return render(request, 'access.html')

def menu_template(request):
    return render(request, 'menu.html')

def works_template(request):
    return render(request, 'works.html')

def staff_template(request):
    return render(request, 'staff.html')

def shop_template(request):
    return render(request, 'shop.html')

def link_template(request):
    return render(request, 'link.html')

def boxbox_template(request):
    return render(request, 'boxbox.html')

def contact_template(request):
    return render(request, 'contact.html')

def recruit_template(request):
    return render(request, 'recruit.html')

def sitemap_template(request):
    return render(request, 'sitemap.html')