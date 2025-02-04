from django.shortcuts import render
from portfolio.models import Project , Prize , Education ,Technology , Persone
from blog.models import Blog , Post , Tag
# Create your views here.


def main_page(request):
	projects  = Project.objects.all()
	technologies = Technology.objects.all()
	persone = Persone.objects.all()
	return render(request,'main.html', {'persone':persone,'projects':projects,'technologies':technologies})


def project_page(request,id):
	project = Project.objects.get(id=id)
	return render(request,'project.html', {'project':project})


def projects_page(request):
	projects = Project.objects.all()
	return render(request,'projects.html', {'projects':projects})

def blogs(request):
	blogs = Blog.objects.all()
	Posts = Post.objects.all()
	lastest_post = Post.objects.all().order_by('-id')[:1]
	return render(request,'blog.html',{'blogs':blogs,'Posts':Posts,'lastest_post':lastest_post})