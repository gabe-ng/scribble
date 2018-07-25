from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm

################### POST ###############

# index - post
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scribble/post_list.html', { 'posts': posts })

# show - post
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'scribble/post_detail.html', { 'post': post })

# create - post
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'scribble/post_form.html', { 'form': form })

# edit - post
def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'scribble/post_form.html', { 'form': form })

# delete - post
def post_delete(request, pk):
    Post.objects.get(pk=pk).delete()
    return redirect('post_list')

################### COMMENT ###############
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'scribble/comment_list.html', { 'comments': comments })

# show - comment
def comment_detail(request, id):
    comments = Comment.objects.get(id=id)
    return render(request, 'scribble/comment_detail.html', { 'comment': comment })

# create - comment
def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('/')
    else:
        form = CommentForm()
    return render(request, 'scribble/comment_form.html', { 'form': form })

# edit - comment
def comment_edit(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=post)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', id=comment.id)
    else:
        form = PostForm(instance=comment)
    return render(request, 'scribble/comment_form.html', { 'form': form })

# delete - comment
def comment_delete(request, id):
    Comment.objects.get(id=id).delete()
    return redirect('comment_list')