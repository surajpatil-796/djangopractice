from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title="Hello Beautiful..."
    template_name="home.html"
    a={"title": my_title}
    return render(request,template_name, a)

