from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .models import Posts

class IndexView(generic.ListView):
	template_name = 'pyblog/index.html'
	context_object_name = 'latest_post_list'
	
	def get_queryset(self):
		return Posts.objects.order_by('-published_date')[:5]
		
class PostDetailView(generic.DetailView):
	model = Posts
	template_name = 'pyblog/detail.html'
	context_object_name = 'post_content'


"""def index(request):
	latest_post_list = Posts.objects.order_by('-published_date')[:5]
	template = loader.get_template('pyblog/index.html')
	context = {'latest_post_list':latest_post_list}
	return HttpResponse(template.render(context, request))

def post_detail(request, post_id):
	post = Posts.objects.get(pk=post_id)
	the_content = post.post_content
	return render(request, 'pyblog/detail.html', {'the_content':the_content})
"""
