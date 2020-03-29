from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Article
from .forms import ArticlePost
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# a= Article.objects.get(id=1)===This would get title=Maggi, content=Mercury

# def article_detail_page(request):
#     a= Article.objects.get(id=1) # query -> database -> data -> django renders it
#     template_name='article_detail_page.html'
#     context= {'object':a}
#     return render(request, template_name, context)


# def article_detail_dynamic(request, post_id):
#     try:
#     a= Article.objects.get(id=post_id) 
#     except Article.DoesNotExist:
#         raise Http404 
#     except ValueError:
#         raise Http404   
#     template_name='article_detail_page.html'
#     context= {'object':a}
#     return render(request, template_name, context)

# GET -> One object
# filter -> [] of objects

def list_view(request):
    qs = Article.objects.all()
    template_name="list.html"
    context = {'object_list': qs}
    return render(request, template_name, context)


def article_detail_dynamic(request, id):
    # this is a validation technique
    a= get_object_or_404(Article, id=id) 
    template_name='article_detail_page.html'
    context= {'object':a}
    return render(request, template_name, context)



def article_detail_update(request, id):
    # this is a validation technique
    a= get_object_or_404(Article, id=id) # looking up the object
    form = ArticlePost(request.POST or None, instance=a) #pass object into modelform as instance
    if form.is_valid():
        form.save()
    template_name='update.html'

    context= {'object':a, 'form':form, "title" : f"Update {a.title}"}
    return render(request, template_name, context)

@staff_member_required
@login_required   #checks if this user have a session
def create_page(request):
    form = ArticlePost(request.POST or None)
    if form.is_valid():
        form.save()
        # form=ContactForm()
        form = ArticlePost()
    template_name='create.html'
    context={"title":"Create Us", 'form':form}
    return render(request, template_name ,context)

def delete_page(request, id):
    obj= get_object_or_404(Article, id=id)
    template_name="delete.html"
    if request.method == 'POST':
        obj.delete()
        return redirect("/blog")         
    context={"object":obj}
    return render(request, template_name, context)



