from django.shortcuts import render, HttpResponse,redirect
from .forms import TaskModelForm
from .models import TaskModel 

# Create your views here.
def getTask(request):
    data = TaskModel.objects.all()
    context = {
        'task_data':data
    }
    return render(request,'index.html',context)

def AddTask(request):
    form_data = TaskModelForm(request.POST)
    if request.method == 'POST':
        if(form_data.is_valid()):
            form_data.save()
            return redirect('home')

    context ={
        "form_data":form_data
    }
    
    return render(request,"add_task.html",context)

def DeleteTask(request,id):
    user_instance = TaskModel.objects.get(pk=id)
    user_instance.delete()
    return redirect('home')

def UpdateCurrentTask(request,id):
    if(request.method == 'POST'):
        tskMdl = TaskModel.objects.get(pk=id)
        task_form = TaskModelForm(request.POST,instance= tskMdl)
        if(task_form.is_valid()):
            task_form.save()
            return redirect('home')
    else:
        tskMdl = TaskModel.objects.get(pk=id)
        task_form = TaskModelForm(instance= tskMdl)
        context = {
            "form_model":task_form
        }     
        return render(request,'update_task.html',context)

