from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . forms import ToDoForm
from.models import Todo

# Create your views here.

def todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form =ToDoForm()
    tasks = Todo.objects.all()
    return render(request,'to_do.html',{'tasks':tasks,'form':form})



def update_task(request,pk):
    task =get_object_or_404(Todo,pk=pk)
    if request.method == 'POST':
        form = ToDoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = ToDoForm(instance=task)
    return render(request,'update_task.html',{'task':task,'form':form})


def delete_task(request,pk):
    task = get_object_or_404(Todo,pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('todo')
    else:
        return render(request, 'delete_task.html', {'task': task})
    

from django.http import JsonResponse

def complete_task(request, task_id):
    task = Todo.objects.get(pk=task_id)
    task.completed = request.POST.get('completed', False)
    task.save()
    return JsonResponse({'completed': task.completed})
