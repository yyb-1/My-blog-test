from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def blog_page(request):
    blogs = Blog.objects
    return render(request, 'blog.html', {'blogs': blogs})

#对博客详情页数据进行定义，所有博客的详情页共用一个html文件，通过抓取不同的ID的blog来控制blog上的不同信息
def blog_text(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)     # PK: primary key
    return render(request, 'blog_text.html', {'blog': blog})