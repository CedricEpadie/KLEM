from django.db import models
from django.contrib.auth.models import AbstractUser

# ==========| Entite pays |==========
class Pays(models.Model):
    '''Model definition for Pays.'''

    nom = models.CharField(max_length=200)
    code_tel = models.CharField(max_length=200)

    class Meta:
        '''Meta definition for Pays.'''

        verbose_name = 'Pays'
        verbose_name_plural = 'Pays'
        ordering = ['nom']

    def __str__(self):
        return self.nom
    

# ==========| Entite ville |==========
class Ville(models.Model):
    '''Model definition for Ville.'''
    
    nom = models.CharField(max_length=200)
    pays = models.ForeignKey(Pays, related_name='pays', on_delete=models.CASCADE, null=True)
    
    class Meta:
        '''Meta definition for Ville.'''

        verbose_name = 'Ville'
        verbose_name_plural = 'Villes'
        ordering = ['nom']
        
    def __str__(self):
        return self.nom
    
# ==========| Class utilisateur qui ne sera pas sauvegarder en base de donnee |==========
class CustomUser(AbstractUser):
    '''Model definition for Utilisateur.'''
    
    address = models.CharField(max_length=300)
    telephone = models.IntegerField()
    ville = models.ForeignKey(Ville, on_delete=models.SET_NULL, null=True, related_name='%(class)s_list')
    is_couturier = models.BooleanField(verbose_name=("Status couturier"), default=False)
    
    def __str__(self):
        return self.nom

# ==========| Entite client |==========
class Client(models.Model):
    '''Model definition for Client.'''
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for Client.'''

        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.nom
    
# ==========| Entite couturier |==========
class Couturier(models.Model):
    '''Model definition for Couturier.'''

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    specialite = models.CharField(max_length=300)

    class Meta:
        '''Meta definition for Couturier.'''

        verbose_name = 'Couturier'
        verbose_name_plural = 'Couturiers'

    def __str__(self):
        return self.nom
    
# ==========| Entite administrateur |==========
class Administrateur(models.Model):
    '''Model definition for Administrateur.'''
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    etat_compte = models.CharField(max_length=200)

    class Meta:
        '''Meta definition for Administrateur.'''

        verbose_name = 'Administrateur'
        verbose_name_plural = 'Administrateurs'

    def __str__(self):
        return self.nom

# ==========| Entite Vetement |==========
class Vetement(models.Model):
    '''Model definition for Vetement.'''
    nom = models.CharField(max_length=200)
    type_vetement = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    prix = models.FloatField()
    image = models.ImageField(upload_to='images/')
    disponibilite = models.CharField(max_length=200)
    
    couturier = models.ForeignKey(Couturier, related_name='couturier', on_delete=models.CASCADE)
    
    class Meta:
        '''Meta definition for etement.'''

        verbose_name = 'Vetement'
        verbose_name_plural = 'Vetements'
        ordering = ['-nom']

    def __str__(self):
        return self.nom
    
# ==========| Entite Mode de paiement |==========
class Mode_Paiement(models.Model):
    '''Model definition for Mode_Paiement.'''
    nom = models.CharField(max_length=200)
    description = models.TextField()
    class Meta:
        '''Meta definition for Mode_Paiement.'''

        verbose_name = 'Mode_Paiement'
        verbose_name_plural = 'Mode_Paiements'
        ordering = ['-nom']

    def __str__(self):
        return self.nom
    
    
# ==========| Entite commande |==========
class Commande(models.Model):
    '''Model definition for Commande.'''
    quantite = models.IntegerField()
    montant_total = models.FloatField()
    etat_commande = models.CharField(max_length=200)
    address_livraison = models.CharField(max_length=200)
    address_facturation = models.CharField(max_length=200)
    remise = models.FloatField()
    etat_livraison = models.CharField(max_length=200)
    date_livraison = models.DateField()
    
    moyen_paiement = models.ForeignKey(Mode_Paiement, related_name='mode_paiement', on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, related_name='client', on_delete=models.SET_NULL, null=True)
    administrateur = models.ForeignKey(Administrateur, related_name='administrateur', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        '''Meta definition for Commande.'''

        verbose_name = 'Commande'
        verbose_name_plural = 'Commandes'
        ordering = ['-etat_commande']

    def __str__(self):
        return self.address_livraison
        
# ==========| Entite vetement_commande |==========
class Vetement_commande(models.Model):
    '''Model definition for Vetement_commande.'''
    date_commande = models.DateField()
    couleur = models.CharField(max_length=200)
    matiere = models.CharField(max_length=200)
    taille = models.CharField(max_length=200)
    
    commande = models.ForeignKey(Commande, related_name='commande', on_delete=models.CASCADE)
    vetement = models.ForeignKey(Vetement, related_name='vetement', on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for Vetement_commande.'''

        verbose_name = 'Vetement_commande'
        verbose_name_plural = 'Vetement_commandes'

    def __str__(self):
        return self.matiere
    
    
# ==========| Entite abonnement |==========
class Abonnement(models.Model):
    '''Model definition for Abonnement.'''
    type_abonnement = models.CharField(max_length=200)
    montant = models.FloatField()
    duree = models.IntegerField()
    frequence_paiement = models.IntegerField()
    data_paiement = models.DateField()
    etat = models.CharField(max_length=200)
    remise = models.FloatField()
    nbre_renouvellement = models.IntegerField()
    
    moyen_paiement = models.ForeignKey(Mode_Paiement, related_name='moyen_paiement', on_delete=models.SET_NULL, null=True)

    class Meta:
        '''Meta definition for Abonnement.'''

        verbose_name = 'Abonnement'
        verbose_name_plural = 'Abonnements'
        ordering= ['-type_abonnement']

    def __str__(self):
        return self.type_abonnement

    
# # ==========| Entite souscription |==========
class Souscription(models.Model):
    '''Model definition for Souscription.'''
    date_debut = models.DateField()
    abonnement = models.ForeignKey(Abonnement, related_name='abonnement', on_delete=models.SET, null=True)
    couturier = models.ForeignKey(Couturier, related_name='couturier_souscription', on_delete=models.SET, null=True)

    class Meta:
        '''Meta definition for Souscription.'''

        verbose_name = 'Souscription'
        verbose_name_plural = 'Souscriptions'
        ordering = ['-abonnement']




# # ==========| Entite devis |==========
class Devis(models.Model):
    '''Model definition for Devis.'''
    montant = models.FloatField()
    description = models.TextField()
    etat_devis = models.CharField(max_length=200)
    date_debut = models.DateField()
    date_fin = models.DateField()
    administrateur = models.ForeignKey(Administrateur, related_name='administrateur_devis', on_delete=models.SET_NULL, null=True)
    couturier = models.ForeignKey(Couturier, related_name='devis_couturier', on_delete=models.SET_NULL, null=True)
    commande = models.ForeignKey(Commande, related_name='devis_commande', on_delete=models.SET_NULL, null=True)

    class Meta:
        '''Meta definition for Devis.'''

        verbose_name = 'Devis'
        verbose_name_plural = 'Devis'
        

    def __str__(self):
        return self.etat_devis
    
# # ==========| Entite tag |==========
class Tag(models.Model):
    '''Model definition for Tag.'''
    description = models.CharField(max_length=300)

    class Meta:
        '''Meta definition for Tag.'''

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.description
    
    
# # ==========| Entite categorie_article |==========
class Categorie_article(models.Model):
    '''Model definition for Categorie_article.'''
    nom = models.CharField(max_length=200)

    class Meta:
        '''Meta definition for Categorie_article.'''

        verbose_name = 'Categorie_article'
        verbose_name_plural = 'Categorie_articles'

    def __str__(self):
        return self.nom
    
# # ==========| Entite article |==========
class Article(models.Model):
    '''Model definition for Arcticle.'''
    nom = models.CharField(max_length=200)
    administrateur = models.ForeignKey(Administrateur, related_name='article_admin', on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie_article, related_name='categorie_article', on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for Arcticle.'''

        verbose_name = 'Arcticle'
        verbose_name_plural = 'Arcticles'

    def __str__(self):
        return self.nom
    
# # ==========| Entite article_tag |==========
class Article_tag(models.Model):
    '''Model definition for Article_tag.'''
    date = models.DateField()
    article = models.ForeignKey(Article, related_name='article', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='tag', on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for Article_tag.'''

        verbose_name = 'Article_tag'
        verbose_name_plural = 'Article_tags'




# # ==========| Entite commentaire |==========

class Commentaire(models.Model):
    '''Model definition for Commentaire.'''
    contenu = models.TextField()
    note = models.IntegerField()
    client = models.ForeignKey(Client, related_name='commentaire_client', on_delete=models.SET_NULL, null=True)
    couturier = models.ForeignKey(Couturier, related_name='commentaire_couturier', on_delete=models.SET_NULL, null=True)
    administrateur = models.ForeignKey(Administrateur, related_name='commentaire_admin', on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, related_name='commentaire_article', on_delete=models.SET_NULL, null=True)
    

    class Meta:
        '''Meta definition for Commentaire.'''

        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

