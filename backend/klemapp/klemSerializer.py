from rest_framework import serializers
from . import models


# =========( Commentaire )===========
class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Commentaire
        fields = '__all__'
        
# =========( Pays )===========
class PaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pays
        fields = '__all__'


# =========( Ville )===========
class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ville
        fields = '__all__'
        
# =========( Client )===========
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'
        
# =========( Couturier )===========
class CouturierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Couturier
        fields = '__all__'
        
# =========( Administrateur )===========
class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Administrateur
        fields = '__all__'
        
# =========( Vetement )===========
class VetementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vetement
        fields = '__all__'
        

# =========( Mode_Paiement )===========
class Mode_PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mode_Paiement
        fields = '__all__'
        

# =========( Commande )===========
class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Commande
        fields = '__all__'
        
# =========( Vetement_commande )===========
class Vetement_commandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vetement_commande
        fields = '__all__'
        
# =========( Abonnement )===========
class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Abonnement
        fields = '__all__'
        
# =========( Souscription )===========
class SouscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Souscription
        fields = '__all__'
        
# =========( Devis )===========
class DevisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Devis
        fields = '__all__'
        
# =========( Tag )===========
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'
        
# =========( Categorie_article )===========
class Categorie_articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categorie_article
        fields = '__all__'
        
# =========( Article )===========
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'
        
# =========( Article_tag )===========
class Article_tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article_tag
        fields = '__all__'