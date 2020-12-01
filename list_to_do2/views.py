from django.shortcuts import render
from .models import item

# Create your views here.

def index(request):
    return render(request, 'list_to_do2/index.html')

def nameView(request):
    return render(
        request, 
        'list_to_do2/perfil.html',
        context={ 'name' : "Pepe Argento"}
        )

def perfilView2(request, name):
    print(name)
    return render(
        request, 
        'list_to_do2/perfil.html',
        context={ 'name' : name}
        )

def itemsList(request):
    list_item=item.objects.all()
    return render(
        request,
        'list_to_do2/items.html',
        context={'items' : list_item}
    )

def itemDetail(request, id):
    """
    el primer id hace referencia a campo base de datos y el segundo al valor recibido de la url,
    el parametro que llega entre parentesis
    """
    item_detail = item.objects.get(id=id)
    return render(
        request,
        'list_to_do2/item_detail.html',
        context={'item' : item_detail }
    )





