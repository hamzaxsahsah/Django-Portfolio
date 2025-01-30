from django.shortcuts import render
from portfolio.models import Project , Prize , Education ,Technology , Persone
# Create your views here.


def main_page(request):
	projects  = Project.objects.all()
	technologies = Technology.objects.all()
	persone = Persone.objects.all()
	return render(request,'main.html', {'persone':persone,'projects':projects,'technologies':technologies})


def project_page(request,id):
	project = Project.objects.get(id=id)
	return render(request,'project.html', {'project':project})