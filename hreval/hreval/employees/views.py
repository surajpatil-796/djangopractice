from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeePost




def list_view(request):
    qs = Employee.objects.all()
    template_name="employees/list.html"
    context = {'object_list': qs}
    return render(request, template_name, context)


def detail_view(request, id):
    # this is a validation technique
    a= get_object_or_404(Employee, id=id) 
    template_name='employees/detail.html'
    context= {'object_list':a}
    return render(request, template_name, context)


def create_page(request):
    form = EmployeePost(request.POST or None)
    if form.is_valid():
        form.save()
        # form=ContactForm()
        form = EmployeePost()
    template_name='create.html'
    context={"title":"Create Us", 'form':form}
    return render(request, template_name ,context)


def update_page(request, id):
    # this is a validation technique
    a= get_object_or_404(Employee, id=id) # looking up the object
    form = EmployeePost(request.POST or None, instance=a) #pass object into modelform as instance
    if form.is_valid():
        form.save()
    template_name='employees/update.html'

    context= {'object_list':a, 'form':form}
    return render(request, template_name, context)

def delete_page(request, id):
    obj= get_object_or_404(Employee, id=id)
    template_name="employees/delete.html"
    if request.method == 'POST':
        obj.delete()
        return redirect('http://127.0.0.1:8000/')         
    context={"object_list":obj}
    return render(request, template_name, context)



# Create your views here.