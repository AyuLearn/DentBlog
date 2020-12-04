from django.shortcuts import render
from .models import Contact, Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contacts = Contact(name=name, email=email, message=message)
        contacts.save()
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {
        'post': post
    }
    return render(request, 'post.html', context)