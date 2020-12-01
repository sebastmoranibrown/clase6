from django.shortcuts import render, redirect
from . import forms
from .models import Item

# Create your views here.

def index(request):
    return render(request, 'list_to_do/index.html')

def AddItem(request):
    error = None
    form = forms.FormularioItem()
    if request.method == "POST":
        form = forms.FormularioItem(request.POST)
        if form.is_valid():
            #Guardas en base de datos
            items = Item(
                title=form.data["title"],
                datail=form.data["datail"]
                )
            items.save()
            return redirect('listItem')
        else:
            #Envio un mensaje de error
            error = "Todo mal"
        


    return render(
            request,
            'list_to_do/addItem.html',
            context={ 'form' : form, 'error' : error }
        )

def ListItem(request):
    # Esto equivale a hacer un SELECT * FROM Item
        listItem = Item.objects.all()
        return render(request, 'list_to_do/list.html', {'list' : listItem})

def DetailItem(request, id):
    item = Item.objects.get(id=id)
    return render(
        request,
        'list_to_do/detail.html',
        { 'item' : item }
    )


