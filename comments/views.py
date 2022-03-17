from django.shortcuts import render, redirect

from .forms import CommentForm

# Create your views here.
def add(request):

    form = CommentForm(request.POST)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment:index')
    else:
        form = CommentForm()

    return render(request,'comments/add.html',{'form':form})