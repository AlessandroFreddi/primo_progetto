from django.shortcuts import render
import random

# Create your views here.
def index_prova_pratica_1(request):
    return render(request,"prova_pratica_1/index_prova_pratica_1.html")

def differenza(request):
    var1 = random.randint(1,20)
    var2 = random.randint(1,20)

    if var1 > var2:
        differenza = var1 - var2
    elif var2 > var1:
        differenza = var2 - var1
    elif var1 == var2:
        differenza = 0

    context = {
        'var1': var1,
        'var2': var2,
        'differenza': differenza
    }
    return render(request,"prova_pratica_1/differenza.html", context)

def pari(request):
    lista = []
    numPari = 0
    numDispari = 0
    for i in range(15):
        var = random.randint(1,20)
        lista.append(var)
        if var%2 == 0:
            numPari += 1
        else:
            numDispari += 1
    
    context = {
        'lista': lista,
        'numPari': numPari,
        'numDispari': numDispari
    }
    

    return render(request,"prova_pratica_1/pari.html", context)