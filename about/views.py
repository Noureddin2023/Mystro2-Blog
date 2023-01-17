from django.shortcuts import render
from .models import About , Skills , Education , Experience , Service , Projects
from posts.models import Post
# Create your views here.
def home(request):
    about = About.objects.last()
    coding_skills = Skills.objects.filter(type='Coding')
    design_skills = Skills.objects.filter(type='Design')
    education = Education.objects.all()
    experience = Experience.objects.all()
    services = Service.objects.all()
    projects = Projects.objects.all()
    posts = Post.objects.all()


    return render(request,'home.html',{'about':about,
       'coding_skills' : coding_skills,
       'design_skills' : design_skills,
       'education' : education,
       'experience' : experience,
       'services' : services,
       'projects' : projects,
       'posts' : posts

       })