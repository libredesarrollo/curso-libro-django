from django.shortcuts import render, redirect

from .forms import ElementForm

# Create your views here.

def add(request):
    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid():
            element = form.save()
            return redirect('element:index')
    else:
        form = ElementForm()

    return render(request,'element/add.html',{'form':form})