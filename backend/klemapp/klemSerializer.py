from rest_framework import serializers
from .models import Commentaire, Pays, Ville, Client, Couturier, Administrateur, Vetement, Mode_Paiement, Commande, Vetement_commande, Abonnement, Souscription, Devis, Tag, Categorie_article, Article, Article_tag


# =========( Commentaire )===========
class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'
        
# =========( Pays )===========
class PaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pays
        fields = '__all__'


# =========( Ville )===========
class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields = '__all__'
        
# =========( Client )===========
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
# =========( Couturier )===========
class CouturierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Couturier
        fields = '__all__'
        
# =========( Administrateur )===========
class AdministrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrateur
        fields = '__all__'
        
# =========( Vetement )===========
class VetementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vetement
        fields = '__all__'
        

# =========( Mode_Paiement )===========
class Mode_PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode_Paiement
        fields = '__all__'
        

# =========( Commande )===========
class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'
        
# =========( Vetement_commande )===========
class Vetement_commandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vetement_commande
        fields = '__all__'
        
# =========( Abonnement )===========
class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = '__all__'
        
# =========( Souscription )===========
class SouscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souscription
        fields = '__all__'
        
# =========( Devis )===========
class DevisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devis
        fields = '__all__'
        
# =========( Tag )===========
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
# =========( Categorie_article )===========
class Categorie_articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie_article
        fields = '__all__'
        
# =========( Article )===========
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        
# =========( Article_tag )===========
class Article_tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article_tag
        fields = '__all__'