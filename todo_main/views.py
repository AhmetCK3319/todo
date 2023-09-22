from django.shortcuts import render
from todoapp.models import Task



def home(request):
    tasks=Task.objects.filter(is_complate=False).order_by('-updated_at')
    complated_task=Task.objects.filter(is_complate=True).order_by('-created_at')
    context={
        'tasks':tasks,
        'complated_task':complated_task,
    }
    return render(request,'home.html',context)