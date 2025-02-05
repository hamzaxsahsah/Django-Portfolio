from django.shortcuts import render
from django.http import HttpResponse
from portfolio.models import Project, Prize, Education, Technology, Persone
from blog.models import Blog, Post, Tag

# Create your views here.


def main_page(request):
    projects = Project.objects.all()
    technologies = Technology.objects.all()
    persone = Persone.objects.all()
    return render(
        request,
        "main.html",
        {"persone": persone, "projects": projects, "technologies": technologies},
    )


def project_page(request, id):
    project = Project.objects.get(id=id)
    return render(request, "project.html", {"project": project})


def projects_page(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def blogs(request):
    blogs = Blog.objects.all()
    Posts = Post.objects.all()[::-1]
    return render(
        request,
        "blog.html",
        {"blogs": blogs, "Posts": Posts},
    )


def post(request, id):
    post = Post.objects.get(id=id)
    return render(
        request,
        "post.html",
        {"post": post},
    )


def contact(request):
    persone = Persone.objects.get(id=1)
    return render(
        request,
        "contact.html",
        {"persone": persone},
    )


def download_resume(request):
    persone = Persone.objects.get(id=1)
    filename = persone.resume.name.split("/")[-1]
    response = HttpResponse(persone.resume, content_type="text/plain")
    response["Content-Disposition"] = "attachment; filename=%s" % filename

    return response
