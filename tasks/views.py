from django.shortcuts import render
from .models import Task
import string
import random
import datetime

def task_list(request):
    getlist = request.POST.getlist('_selected_action')
    action = request.POST.get('action')
    message = ''
    if action == 'delete':
        Task.objects.filter(id__in=getlist, token=request.COOKIES.get('token')).delete()
        message = 'Tasks deleted'
    elif action == 'complete':
        Task.objects.filter(id__in=getlist, token=request.COOKIES.get('token')).update(completed=True, updated_at=datetime.datetime.now())
        message = 'Tasks completed'
    elif action == 'add_task':
        Task.objects.create(title=request.POST.get('title'), token=request.COOKIES.get('token'))
        message = 'Task added'
    tasks = Task.objects.filter(token=request.COOKIES.get('token')).order_by('-id').all()
    context = {'tasks': tasks, 'message': message}
    response = render(request, 'tasks/task_list.html', context)
    if not request.COOKIES.get('token'):
        response.set_cookie('token', ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)), expires=31539600)
    if request.COOKIES.get('token'):
        response.set_cookie('token', request.COOKIES.get('token'), expires=31649600)  # update cookie expiration 1 year
    return response
