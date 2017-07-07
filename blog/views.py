from django.shortcuts import render
from .models import Post 
from django.utils import timezone

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#posts is queryset variable

	return render(request, 'blog/post_list.html',{'posts':posts})



# Create your views here.
