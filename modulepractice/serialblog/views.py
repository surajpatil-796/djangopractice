from django.shortcuts import render, get_object_or_404
from .models import Task
from .forms import TaskPost




def list_view(request):
    qs = Task.objects.all()
    template_name="serialblog/list.html"
    context = {'object_list': qs}
    return render(request, template_name, context)


def detail_view(request, id):
    # this is a validation technique
    a= get_object_or_404(Task, id=id) 
    template_name='serialblog/detail.html'
    context= {'object_list':a}
    return render(request, template_name, context)


