from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import AddPostForm

def homePage(request):
    return render(request, "index.html")

def abouPage(request):
    return render(request, "about.html")

def newsPage(request):
    posts = Post.objects.all().order_by('-postDate')
    return render(request, "news.html", {
        'posts': posts
    })

def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post-detail.html", {
        'post': post
    })

def addPost(request):
    form = AddPostForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("newsPage")
    else:
        form = AddPostForm()

    return render(request, "add-post.html", {
        'form': form
    })

def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("newsPage")

    return render(request, "delete-post.html", {
        'post': post
    })

def editPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = AddPostForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect("newsPage")
    else:
        form = AddPostForm()

    return render(request, "edit-post.html", {
        'post': post,
        'form': form
    })