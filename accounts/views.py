from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST) #crea l'istanza con l'input dell'utente
        
        if form.is_valid(): #effettua la validazione
            form.save()
            return redirect('login') #eventualmente da personalizzare
            
    else: #richiesta di tipo get mostro il form vuoto
        form = SignUpForm()
        
    return render(request, 'registration/signup.html', {'form': form})