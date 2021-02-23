from django.shortcuts import render, get_object_or_404
from .models import Blogs

# Create your views here.
def all_blogs(request):
    blog=Blogs.objects.order_by('-date')
    return render(request,'blog/blog.html' , {'blogs':blog})

def details(request,blog_id):
    id=get_object_or_404(Blogs,pk=blog_id)
    return render (request,'blog/details.html', {'id':id})
