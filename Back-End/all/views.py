from django.shortcuts import render , get_object_or_404 , redirect
from musics.models import Music_Class , Comment
from musics.forms  import CommentForm
from taggit.models import Tag


# Create your views here.

def all_home(request):
    data = Music_Class.objects.all()
    context = {
        "postsindb" : data,
    }
    return render(request, 'all/home.html',context=context)
"""
def all_home(request):
    data = Music_Class.objects.all()
    tags_with_posts = []
    all_tags = Tag.objects.all()
    
    for tag in all_tags:
        posts = Music_Class.objects.filter(Genres__name__in=[tag.name])
        tags_with_posts.append({
            'tag': tag,
            'posts': posts,
        })

    context = {
        "tags_with_posts": tags_with_posts,
    }
    return render(request, 'all/home.html', context=context)
"""

def det_view(request, blog_id):
    # Retrieve the music article object
    data = get_object_or_404(Music_Class, id=blog_id)
    #viewer number code
    data.viewer = data.viewer + 1
    data.save()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.article = data
            new_comment.save()
            return redirect('detail', blog_id=blog_id)  # Redirect to the same article page
    else:
        form = CommentForm()

    context = {
        "postsindb": data,
        "form": form,
    }
    return render(request, 'all/det_view.html', context=context)

def search(request):
    if request.method =="POST":
        query_name =request.POST.get('q')
        if query_name:
            resualts = Music_Class.objects.filter(title__icontains=query_name) | \
                      Music_Class.objects.filter(artist__username__icontains=query_name)
            context = {
                "postsindb" : resualts,
            }
            return render(request, 'all/home.html',context=context)
        else:
            return render(request, 'all/home.html')