from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Blog

# Create your views here.
def all_blogs(request):
    b_log = Blog.objects.all().order_by('blog_date')#shows all the blogs/articles
    #b_log = Blog.objects.order_by('-blog_date')[:4] limits the blogs/articles shown as per the most recent ones and the number to show
    return render(request, 'blog/all_blogs.html',{'blog':b_log})

def detail(request,blog_id):
    try:
        b_log = get_object_or_404(Blog, pk=blog_id)
    except:
        return render(request,'blog/error.html')

    return render(request,'blog/detail.html',{'blog':b_log})
