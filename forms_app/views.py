from django.shortcuts import render
from .forms import FormContatto
from .models import Contatto
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

# Create your views here.
# Create your views here.
def contatti(request):

    # Se la richiesta è di tipo POST, allora possiamo processare i dati
    if request.method == "POST":

        # Creiamo l'istanza del form e la popoliamo con i dati della POST request (processo di "binding")
        form = FormContatto(request.POST)

        # is_valid() controlla se il form inserito è valido:
        if form.is_valid():
            # a questo punto possiamo usare i dati validi!
            # tenere a mente che cleaned_data["nome_dato"] ci permette di accedere ai dati validati e convertiti in tipi standard di Python
            print ("Salvo il contatto nel database")
            nuovo_contatto = form.save()
            print("new_post: ", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)

            # ringrazio l'utente per averci contattato - volendo possiamo effettuare un redirect a una pagina specifica
            return HttpResponse("<h1>Grazie per averci contattato!</h1>")

    # Se la richiesta HTTP usa il metodo GET o qualsiasi altro metodo, allora creo il form di default vuoto
    else:
        form = FormContatto()

    # arriviamo a questo punto se si tratta della prima volta che la pagina viene richiesta(con metodo GET), o se il form non è valido e ha errori
    context = {"form": form}
    return render(request, "forms_app/contatto.html", context)


def lista_contatti(request):
    contatti = Contatto.objects.all()
    context = {
        'contatti': contatti
    }
    return render(request, "forms_app/lista_contatti.html", context)

@login_required(login_url="/accounts/login")
def modifica_contatto(request, pk):

    contatto = get_object_or_404(Contatto, id=pk)
    if request.method == "GET": #prima chiamata get per caricare il form
        form = FormContatto(instance=contatto) #al costruttore del form passo il contatto prelevato dal db
    if request.method == "POST": #seconda chiamata post per modificare il contatto
        form = FormContatto(request.POST, instance=contatto) #ora passo oltre al contatto prelevato dal db anche i dati modificati
        if form.is_valid():
            form.save()
            return redirect('forms_app:lista-contatti') # url che reindirizza alla pagina lista_contatti.html

    context={'form': form, 'contatto': contatto}
    return render(request, 'forms_app/modifica_contatto.html', context)

@staff_member_required(login_url="/accounts/login")
def elimina_contatto(request, pk):
    contatto = get_object_or_404(Contatto, id=pk)
    if request.method == "POST": 
        contatto.delete()
    context= {'contatto': contatto}
    return render(request, 'forms_app/elimina_contatto.html', context)