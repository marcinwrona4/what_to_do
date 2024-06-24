from django.shortcuts import render, redirect

from .models import Entry
from .forms import EntryForm

def index(request):
    entries = Entry.objects.order_by('-date_added')

    form = EntryForm()

    if request.method == "POST":
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/')
        
    context = {'entries': entries, 'form': form}
    return render(request, 'what_to_do_app/index.html', context)

def task_update(request, pk):
    task = Entry.objects.get(id=pk)
    
    if request.method != 'POST':

        form = EntryForm(instance=task)
    else:
        form = EntryForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {"form": form, "task": task}
    return render(request, "what_to_do_app/task_update.html", context)

def task_delete(request, pk):
    task = Entry.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    
    context = {"task": task}
    return render(request, 'what_to_do_app/task_delete.html', context)

