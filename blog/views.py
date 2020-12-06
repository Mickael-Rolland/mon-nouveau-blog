from django.shortcuts import render
from django.utils import timezone
from .models import Post, Equipement, Animal
from django.shortcuts import render, get_object_or_404

# Create your views here.


def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'blog/animal_list.html', {'animals': animals})


def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    return render(request, 'blog/animal_detail.html', {'animal': animal})
