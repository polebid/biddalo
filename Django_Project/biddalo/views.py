from django.shortcuts import render
from django.views.generic import ListView

from biddalo.models import Post

# Create your views here.

class ListPost(ListView):
    
    model = Post
    template_name = 'Index.html'
