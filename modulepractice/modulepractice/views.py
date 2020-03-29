from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    # "view is kind off python function that can render out some stuff"
    # request something we get response
    # return HttpResponse("<h1>Hello World </h1>")
    
    # render takes request and gives actual template name
    my_title="Hello Beautiful..."
    return render(request,"home.html", {"title": my_title})

def about_page(request):
    return HttpResponse("<h1>About Us </h1>")


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # form=ContactForm()

        print(form.cleaned_data)
    template_name='form.html'
    context={"title":"Contact Us", 'form':form}
    return render(request, template_name ,context)
    
    # return render(request, "form.html",{'title':"Contact Us"})
    # return HttpResponse("<h1>Contact Us </h1>")