
from .models import Comment
from django.shortcuts import render, redirect

from .forms import CommentForm

# Create your views here.
def add(request):

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            #return redirect('comment:index')
    else:
        form = CommentForm()

    return render(request,'comments/add.html',{'form':form})


def index(request):
    comments = Comment.objects.all()
    return render(request,'comments/index.html',{'comments':comments})

    #paginator = Paginator(comments,5)

    #page_number = request.GET.get('page')
    #comments_page = paginator.get_page(page_number)

    #return render(request,'index.html',{'comments':comments})

def update(request, pk):

    #comment = get_object_or_404(Comment, pk=pk)

    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
    else:
        form = CommentForm(instance=comment)

    return render(request,'comments/add.html',{'form':form, 'comment': comment})

def delete(request, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        comment.delete()
            #return redirect('comment:update',pk=comment.id)