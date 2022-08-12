
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from . models import *
from .forms import TodoForm

# Create your views here.

def home(request):
    list1 = list(Todo.objects.all().values())
    dict1 = {'list1':list1}
    print(dict1)
    return render(request,'home.html',dict1)


def create(request):
    tasks = request.POST.get('tasks')
    description = request.POST.get('description')

    # todo_dict = {'task':tasks, 'desc':description}
    # todo_item = Todo(**todo_dict)
    todo_item = Todo(task = tasks,desc = description)  # ---> or use commented
    todo_item.save()
    return redirect('home')


def delete(request,pk):
    todo_item = Todo.objects.get(id=pk)
    todo_item.delete()
    return redirect('home')


def update(request,pk):
    todo_item = Todo.objects.get(id=pk)
    tasks = request.POST.get('tasks')
    description = request.POST.get('description')

    todo_item.save()
    return redirect('home')



def formview(request,pk=None):

    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            Todo.objects.create(**form.cleaned_data)
        return redirect('formview')

    elif request.method == 'GET':
        form = TodoForm
        if pk!=None:
            item_to_delete = Todo.objects.get(id=pk)
            item_to_delete ()
            # print(Todo.objects.all().values())
            list2 = list(Todo.objects.all().values())
            # print(list2)
        
        return render(request,'forms1.html',{'form' :form,'lists': list2})

