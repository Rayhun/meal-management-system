from django.shortcuts import HttpResponse
from meal.models import ToDo, NeedItem


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
        print(e)
        todo = None
    return HttpResponse(todo.is_completed)


def need_item_load_ajax(request):
    """
    Load ajax view.
    """
    id = request.GET.get('id')
    try:
        item = NeedItem.objects.get(id=id)
        if item.status:
            item.status = False
        else:
            item.status = True
        item.save()
    except Exception as e:
        print(e)
        item = None
    return HttpResponse(item.status)
