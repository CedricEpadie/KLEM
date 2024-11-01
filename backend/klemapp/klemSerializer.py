from rest_framework import serializers
from rest_framework.validators import UniqueValidator
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

# ========( CustomUser )========
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
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
        
# =======( Register )==============
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=models.CustomUser.objects.all())]
    )
    password = serializers.CharField(write_only=True)
    last_name = serializers.CharField(required=True)
    
    class Meta:
        model = models.CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'pays', 'ville', 'address', 'telephone', 'is_couturier')

    def create(self, validated_data):
        user = models.CustomUser.objects.create_user(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            password = validated_data['password'],
            pays = validated_data.get('pays', None),
            ville = validated_data.get('ville', None),
            address = validated_data.get('address', ''),
            telephone = validated_data.get('telephone', None),
            is_couturier = validated_data.get('is_couturier', False)
        )
        
        return user
    
# =======( Login )========
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = models.CustomUser
        fields = ('username', 'password')

# =======( Logout )======
class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id',)