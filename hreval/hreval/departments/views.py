from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Department
from .forms import DepartmentPost

def list_view(request):
    qs = Department.objects.all()
    template_name="departments/list.html"
    context = {'object': qs}
    return render(request, template_name, context)


def detail_view(request, id):
    # this is a validation technique
    a= get_object_or_404(Department, id=id) 
    template_name='departments/detail.html'
    context= {'object':a}
    return render(request, template_name, context)


# def create_page(request):
#     form = RolePost(request.POST or None)
#     if form.is_valid():
#         form.save()
#         # form=ContactForm()
#         form = RolePost()
#     template_name='create.html'
#     context={"title":"Create Us", 'form':form}
#     return render(request, template_name ,context)


def update_page(request, id):
    # this is a validation technique
    a= get_object_or_404(Department, id=id) # looking up the object
    form = DepartmentPost(request.POST or None, instance=a) #pass object into modelform as instance
    if form.is_valid():
        form.save()
    template_name='departments/update.html'

    context= {'object':a, 'form':form}
    return render(request, template_name, context)

def delete_page(request, id):
    obj= get_object_or_404(Department, id=id)
    template_name="departments/delete.html"
    if request.method == 'POST':
        obj.delete()
        return redirect("/home")         
    context={"object":obj}
    return render(request, template_name, context)



