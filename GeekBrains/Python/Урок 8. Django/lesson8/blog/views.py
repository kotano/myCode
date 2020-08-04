# from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Post 

# Create your views here.
def post_list(request):

    post_list = Post.objects.all()

    return render_to_response('blog/post_list.html', {'post_list': post_list})
