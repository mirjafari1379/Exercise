from django.shortcuts import render

from blog.models import Post

def addpost(request):
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get("title"))
        print(request.POST.get("content"))
        Post.objects.create(title=request.POST.get("title"), content=request.POST.get("content"))
    return render(request, "addPost.html")
