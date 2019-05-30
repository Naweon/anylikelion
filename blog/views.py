from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForms
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    blog_all = Blog.objects.all
    context = {"blog_all":blog_all}
    return render(request,'index.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        forms = BlogForms(request.POST)

        if forms.is_valid:                     #장고에서 기본적으로 제공하는 유효성검사. 
            forms.save()
            return redirect('new')
    forms = BlogForms()
    return render(request,'new.html', {'forms':forms}) 

def detail(request, blog_id):
        blog_one =get_object_or_404(Blog,id=blog_id)
        context = {'blog_one':blog_one}
        return render(request,'detail.html',context)

def edit(request, blog_id):
        blog_edit = get_object_or_404(Blog,id = blog_id)
        forms = BlogForms(instance=blog_edit)
        if request.method == 'POST':
                forms = BlogForms(request.POST,instance=blog_edit)
                if forms.is_valid:
                        forms.save()
                        return redirect('index')
        return render(request,'new.html',{'forms':forms})

def delete(request, blog_id):
        blog_delete = get_object_or_404(Blog,id = blog_id)
        blog_delete.delete()

        return redirect('index')
