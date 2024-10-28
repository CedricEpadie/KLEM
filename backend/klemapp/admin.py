from django.contrib import admin
from . import models

admin.site.register(
    [
        models.Abonnement, 
        models.Administrateur,
        models.Vetement,
        models.Mode_Paiement,
        models.Commande,
        models.Vetement_commande,
        models.Souscription,
        models.Devis,
        models.Tag,
        models.Categorie_article,
        models.Article,
        models.Commentaire,
        models.Pays,
        models.Ville,
        models.Client,
        models.Couturier,
        models.Article_tag
    ]
)
