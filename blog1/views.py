from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'first Post Content',
#         'date_posted': 'August-27-2018'
#     },
#      {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'second Post Content',
#         'date_posted': 'August-28-2018'
#     }
# ]  Dummy Data :))))))))))


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog1/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog1/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'blog1/about.html', {'title': 'About'})
