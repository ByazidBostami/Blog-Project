from django.shortcuts import render, redirect
from .import forms
from .import models 
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Post



def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    
    return redirect ('homepage')

def search_posts(request):
    query = request.GET.get('q')
    results = []
    
    if query:
        results = models.Post.objects.filter(
            Q(title__icontains=query) | Q(category__name__icontains=query)
        )
    
    return render(request, 'search_results.html', {'results': results, 'query': query})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'post_detail.html', {'post': post})
