from django.shortcuts import render, redirect
from .models import List, Item
from .forms import CheckedForm

# Create your views here.

def index(request):
    return render(request, 'to_do_app/index.html')

def ListView(request):
    my_list = List.objects.all()
    # Las guardo en una variable de contexto
    context = {"list" : my_list}
    return render(request, 'to_do_app/listV.html', context=context)

def ListItemsViews(request, list_id):
    #traer de base de datos los items de lista
    #all---> me trae todo
    #get---> trae solo una fila dentro de un ()
    #filter--> trae todas las filas dentro de un ()
    items_list = Item.objects.filter(list_father = list_id)
    #Guardo en variable de contexto
    context = { "items" : items_list }
    return render(request, 'to_do_app/itemV.html',context=context)

def ListItemsViewsOtherTemplate(request, list_id):
    #traer de base de datos los items de lista
    #all---> me trae todo
    #get---> trae solo una fila dentro de un ()
    #filter--> trae todas las filas dentro de un ()
    items_list = Item.objects.filter(list_father = list_id)
    #Guardo en variable de contexto
    context = { "items" : items_list }
    return render(request, 'to_do_app/itemV2.html',context=context)


def ChangeStateItemViews(request, id):
    if request.method == "POST":
        form = CheckedForm(request.POST)
        form.is_valid()
        value = form.cleaned_data["checked"]

        item = Item.objects.get(id=id)
        item.checked = True
        item.save()
    else:
        print("No, no es post")
    return redirect('lists')