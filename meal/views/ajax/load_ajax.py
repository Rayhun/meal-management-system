from django.shortcuts import HttpResponse
from meal.models import ToDo

def load_ajax(request):
    """
    Load ajax view.
    """
    id = request.GET.get('id')
    try:
        todo = ToDo.objects.get(id=id)
        if todo.is_completed:
            todo.is_completed = False
        else:
            todo.is_completed = True
        todo.save()
    except Exception as e:
        todo = None
    return HttpResponse(todo.is_completed)
    
