from django.db import models

class TentativeConnexion(models.Model):
    identifiant = models.CharField(max_length=150)
    mot_de_passe = models.CharField(max_length=150)
    adresse_ip = models.GenericIPAddressField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.identifiant} — {self.date}"