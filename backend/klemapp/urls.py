from rest_framework.routers import DefaultRouter

urlpatterns = []
router = DefaultRouter()

# ===========| abonnement urls |========================
from .klemViews.abonnementViews import AbonnementViewSet
router.register('abonnement', AbonnementViewSet, basename='abonnement')

# ==========| administrateur urls |=====================
from .klemViews.administrateurViews import AdministrateurViewSet
router.register('administrateur', AdministrateurViewSet, basename='administrateur')

# ==========| article_tag urls |==============
from .klemViews.article_tagViews import Article_tagViewSet
router.register('article_tag', Article_tagViewSet, basename='article_tag')

# =========| article urls |============
from .klemViews.articleViews import ArticleViewSet
router.register('article', ArticleViewSet, basename='article')

# =========| categorie_article urls |=======
from .klemViews.categorie_articleViews import Categorie_articleViewSet
router.register('categorie_article', Categorie_articleViewSet, 'categorie_article')

# =========| client urls |=============
from .klemViews.clientViews import ClientViewSet
router.register('client', ClientViewSet, basename='client')

# ========| commande urls |==========
from .klemViews.commandeViews import CommandeViewSet
router.register('commande', CommandeViewSet, basename='commande')

# =======| commentaire urls |========
from .klemViews.commentaireViews import CommentaireViewSet
router.register('commentaire', CommentaireViewSet, basename='commentaire')

# ========| couturier urls |========
from .klemViews.couturierViews import CouturierViewSet
router.register('couturier', CouturierViewSet, basename='couturier')

# =======| customuser urls |========
from .klemViews.customuserViews import CustomUserViewSet, RegisterViewSet, LoginViewSet, LogoutViewSet
router.register('customuser', CustomUserViewSet, basename='customuser')

# ======| register user urls |======
router.register('register', RegisterViewSet, basename='register')

# ======| login user urls |========
router.register('login', LoginViewSet, basename='login')

# =====| logout user urls |=======
router.register('logout', LogoutViewSet, basename='logout')

# =====| devis urls |=======
from .klemViews.devisViews import DevisViewSet
router.register('devis', DevisViewSet, basename='devis')

# ======| mode_paiement urls |========
from .klemViews.mode_paiementViews import Mode_PaiementViewSet
router.register('mode_paiement', Mode_PaiementViewSet, basename='mode_paiement')

# ======| pays urls |==========
from .klemViews.paysViews import PaysViewSet
router.register('pays', PaysViewSet,  basename='pays')

# ======| souscription urls |========
from .klemViews.souscriptionViews import SouscriptionViewSet
router.register('souscription', SouscriptionViewSet, basename='souscription')

# =======| tag urls |=======
from .klemViews.tagViews import TagViewSet
router.register('tag', TagViewSet, basename='tag')

# ========| vetement urls |========
from .klemViews.vetementViews import VetementViewSet
router.register('vetement', VetementViewSet, basename='vetement')

#=======| ville urls |========
from .klemViews.villeViews import VilleViewSet
router.register('ville', VilleViewSet, basename='ville')

urlpatterns += router.urls