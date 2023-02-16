from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post


# posts = [
#       {'title':'Blog Post 1','author':'Anthony','date_posted':'Feb 15, 2023','content':'The great journey of django'},
#       {'title':'Blog Post 3','author':'Tirop','date_posted':'Feb 20, 2023','content':'The Marvelous journey of django'}
#     ]

def home(request):
    context = {'posts':Post.objects.all(), 'title':'Home'}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})