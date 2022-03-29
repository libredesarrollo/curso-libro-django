
from .models import Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .forms import CommentForm

# Create your views here.
def add(request):
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comments:index')
    else:
        form = CommentForm()

    return render(request,'comments/add.html',{'form':form})


def index(request):
    print(Comment.objects.get(pk=1))
    comments = Comment.objects.all()
    paginator = Paginator(comments,2)

    page_number = request.GET.get('page')
    comments_page = paginator.get_page(page_number)
    return render(request,'comments/index.html',{'comments':comments_page})



    #return render(request,'index.html',{'comments':comments})

def update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    #comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            return redirect('comments:index')
    else:
        form = CommentForm(instance=comment)

    return render(request,'comments/add.html',{'form':form, 'comment': comment})

def delete(request, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        comment.delete()
    return redirect('comments:index')