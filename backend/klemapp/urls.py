from .klemViews.commentaireViews import CommentaireCreateView, CommentaireListView, CommentaireUpdateView, CommentaireDeleteView
# from .views import register, login_view, InscriptionView, TestUrl
from django.urls import path
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # path('test/', CommentaireCreateView, name='testUrl'),
    # path('inscription/', InscriptionView.as_view()),
    # path('register/', register, name='register'),
    # path('login/', login_view, name='login'),
   
]




# ===========| commentaire urls |========================
commentaireRouteur = DefaultRouter()
# commentaireRouteur.register('commentaire_rest', commentaireViewset, basename='commentaire_viewset' )
commentaire_urls = [
    path('klem/commentaire/new/', CommentaireCreateView.as_view(), name='commentaire-create'),
    path('klem/commentaire/list/', CommentaireListView.as_view(), name='commentaire-list'),
    path('klem/commentaire/<int:id>/', CommentaireUpdateView.as_view(), name='commentaire-update'),
    path('klem/commentaire/<int:id>/delete/', CommentaireDeleteView.as_view(), name='commentaire-delete'),
]
urlpatterns += commentaire_urls + commentaireRouteur.urls



# ===========| pays urls |========================
from .klemViews.paysViews import PaysCreateView, PaysListView, PaysUpdateView, PaysDeleteView

paysRouteur = DefaultRouter()
# paysRouteur.register('pays_rest', paysViewset, basename='pays_viewset' )
pays_urls = [
    path('klem/pays/new/', PaysCreateView.as_view(), name='pays-create'),
    path('klem/pays/list/', PaysListView.as_view(), name='pays-list'),
    path('klem/pays/<int:id>/', PaysUpdateView.as_view(), name='pays-update'),
    path('klem/pays/<int:id>/delete/', PaysDeleteView.as_view(), name='pays-delete'),
]
urlpatterns += pays_urls + paysRouteur.urls



# ===========| ville urls |========================
from .klemViews.villeViews import VilleCreateView, VilleListView, VilleUpdateView, VilleDeleteView

villeRouteur = DefaultRouter()
# villeRouteur.register('ville_rest', villeViewset, basename='ville_viewset' )
ville_urls = [
    path('klem/ville/new/', VilleCreateView.as_view(), name='ville-create'),
    path('klem/ville/list/', VilleListView.as_view(), name='ville-list'),
    path('klem/ville/<int:id>/', VilleUpdateView.as_view(), name='ville-update'),
    path('klem/ville/<int:id>/delete/', VilleDeleteView.as_view(), name='ville-delete'),
]
urlpatterns += ville_urls + villeRouteur.urls


# ===========| client urls |========================
from .klemViews.clientViews import ClientCreateView, ClientListView, ClientUpdateView, ClientDeleteView

clientRouteur = DefaultRouter()
# clientRouteur.register('client_rest', clientViewset, basename='client_viewset' )
client_urls = [
    path('klem/client/new/', ClientCreateView.as_view(), name='client-create'),
    path('klem/client/list/', ClientListView.as_view(), name='client-list'),
    path('klem/client/<int:id>/', ClientUpdateView.as_view(), name='client-update'),
    path('klem/client/<int:id>/delete/', ClientDeleteView.as_view(), name='client-delete'),
]
urlpatterns += client_urls + clientRouteur.urls




# ===========| couturier urls |========================
from .klemViews.couturierViews import CouturierCreateView, CouturierListView, CouturierUpdateView, CouturierDeleteView

couturierRouteur = DefaultRouter()
# couturierRouteur.register('couturier_rest', couturierViewset, basename='couturier_viewset' )
couturier_urls = [
    path('klem/couturier/new/', CouturierCreateView.as_view(), name='couturier-create'),
    path('klem/couturier/list/', CouturierListView.as_view(), name='couturier-list'),
    path('klem/couturier/<int:id>/', CouturierUpdateView.as_view(), name='couturier-update'),
    path('klem/couturier/<int:id>/delete/', CouturierDeleteView.as_view(), name='couturier-delete'),
]
urlpatterns += couturier_urls + couturierRouteur.urls



# ===========| administrateur urls |========================
from .klemViews.administrateurViews import AdministrateurCreateView, AdministrateurListView, AdministrateurUpdateView, AdministrateurDeleteView

administrateurRouteur = DefaultRouter()
# administrateurRouteur.register('administrateur_rest', administrateurViewset, basename='administrateur_viewset' )
administrateur_urls = [
    path('klem/administrateur/new/', AdministrateurCreateView.as_view(), name='administrateur-create'),
    path('klem/administrateur/list/', AdministrateurListView.as_view(), name='administrateur-list'),
    path('klem/administrateur/<int:id>/', AdministrateurUpdateView.as_view(), name='administrateur-update'),
    path('klem/administrateur/<int:id>/delete/', AdministrateurDeleteView.as_view(), name='administrateur-delete'),
]
urlpatterns += administrateur_urls + administrateurRouteur.urls



# ===========| vetement urls |========================
from .klemViews.vetementViews import VetementCreateView, VetementListView, VetementUpdateView, VetementDeleteView

vetementRouteur = DefaultRouter()
# vetementRouteur.register('vetement_rest', vetementViewset, basename='vetement_viewset' )
vetement_urls = [
    path('klem/vetement/new/', VetementCreateView.as_view(), name='vetement-create'),
    path('klem/vetement/list/', VetementListView.as_view(), name='vetement-list'),
    path('klem/vetement/<int:id>/', VetementUpdateView.as_view(), name='vetement-update'),
    path('klem/vetement/<int:id>/delete/', VetementDeleteView.as_view(), name='vetement-delete'),
]
urlpatterns += vetement_urls + vetementRouteur.urls



# ===========| mode_paiement urls |========================
from .klemViews.mode_paiementViews import Mode_PaiementCreateView, Mode_PaiementListView, Mode_PaiementUpdateView, Mode_PaiementDeleteView

mode_paiementRouteur = DefaultRouter()
# mode_paiementRouteur.register('mode_paiement_rest', mode_paiementViewset, basename='mode_paiement_viewset' )
mode_paiement_urls = [
    path('klem/mode_paiement/new/', Mode_PaiementCreateView.as_view(), name='mode_paiement-create'),
    path('klem/mode_paiement/list/', Mode_PaiementListView.as_view(), name='mode_paiement-list'),
    path('klem/mode_paiement/<int:id>/', Mode_PaiementUpdateView.as_view(), name='mode_paiement-update'),
    path('klem/mode_paiement/<int:id>/delete/', Mode_PaiementDeleteView.as_view(), name='mode_paiement-delete'),
]
urlpatterns += mode_paiement_urls + mode_paiementRouteur.urls



# ===========| commande urls |========================
from .klemViews.commandeViews import CommandeCreateView, CommandeListView, CommandeUpdateView, CommandeDeleteView

commandeRouteur = DefaultRouter()
# commandeRouteur.register('commande_rest', commandeViewset, basename='commande_viewset' )
commande_urls = [
    path('klem/commande/new/', CommandeCreateView.as_view(), name='commande-create'),
    path('klem/commande/list/', CommandeListView.as_view(), name='commande-list'),
    path('klem/commande/<int:id>/', CommandeUpdateView.as_view(), name='commande-update'),
    path('klem/commande/<int:id>/delete/', CommandeDeleteView.as_view(), name='commande-delete'),
]
urlpatterns += commande_urls + commandeRouteur.urls


# ===========| abonnement urls |========================
from .klemViews.abonnementViews import AbonnementCreateView, AbonnementListView, AbonnementUpdateView, AbonnementDeleteView

abonnementRouteur = DefaultRouter()
# abonnementRouteur.register('abonnement_rest', abonnementViewset, basename='abonnement_viewset' )
abonnement_urls = [
    path('klem/abonnement/new/', AbonnementCreateView.as_view(), name='abonnement-create'),
    path('klem/abonnement/list/', AbonnementListView.as_view(), name='abonnement-list'),
    path('klem/abonnement/<int:id>/', AbonnementUpdateView.as_view(), name='abonnement-update'),
    path('klem/abonnement/<int:id>/delete/', AbonnementDeleteView.as_view(), name='abonnement-delete'),
]
urlpatterns += abonnement_urls + abonnementRouteur.urls


# ===========| souscription urls |========================
from .klemViews.souscriptionViews import SouscriptionCreateView, SouscriptionListView, SouscriptionUpdateView, SouscriptionDeleteView

souscriptionRouteur = DefaultRouter()
# souscriptionRouteur.register('souscription_rest', souscriptionViewset, basename='souscription_viewset' )
souscription_urls = [
    path('klem/souscription/new/', SouscriptionCreateView.as_view(), name='souscription-create'),
    path('klem/souscription/list/', SouscriptionListView.as_view(), name='souscription-list'),
    path('klem/souscription/<int:id>/', SouscriptionUpdateView.as_view(), name='souscription-update'),
    path('klem/souscription/<int:id>/delete/', SouscriptionDeleteView.as_view(), name='souscription-delete'),
]
urlpatterns += souscription_urls + souscriptionRouteur.urls


# ===========| devis urls |========================
from .klemViews.devisViews import DevisCreateView, DevisListView, DevisUpdateView, DevisDeleteView

devisRouteur = DefaultRouter()
# devisRouteur.register('devis_rest', devisViewset, basename='devis_viewset' )
devis_urls = [
    path('klem/devis/new/', DevisCreateView.as_view(), name='devis-create'),
    path('klem/devis/list/', DevisListView.as_view(), name='devis-list'),
    path('klem/devis/<int:id>/', DevisUpdateView.as_view(), name='devis-update'),
    path('klem/devis/<int:id>/delete/', DevisDeleteView.as_view(), name='devis-delete'),
]
urlpatterns += devis_urls + devisRouteur.urls


# ===========| tag urls |========================
from .klemViews.tagViews import TagCreateView, TagListView, TagUpdateView, TagDeleteView

tagRouteur = DefaultRouter()
# tagRouteur.register('tag_rest', tagViewset, basename='tag_viewset' )
tag_urls = [
    path('klem/tag/new/', TagCreateView.as_view(), name='tag-create'),
    path('klem/tag/list/', TagListView.as_view(), name='tag-list'),
    path('klem/tag/<int:id>/', TagUpdateView.as_view(), name='tag-update'),
    path('klem/tag/<int:id>/delete/', TagDeleteView.as_view(), name='tag-delete'),
]
urlpatterns += tag_urls + tagRouteur.urls


# ===========| categorie_article urls |========================
from .klemViews.categorie_articleViews import Categorie_articleCreateView, Categorie_articleListView, Categorie_articleUpdateView, Categorie_articleDeleteView

categorie_articleRouteur = DefaultRouter()
# categorie_articleRouteur.register('categorie_article_rest', categorie_articleViewset, basename='categorie_article_viewset' )
categorie_article_urls = [
    path('klem/categorie_article/new/', Categorie_articleCreateView.as_view(), name='categorie_article-create'),
    path('klem/categorie_article/list/', Categorie_articleListView.as_view(), name='categorie_article-list'),
    path('klem/categorie_article/<int:id>/', Categorie_articleUpdateView.as_view(), name='categorie_article-update'),
    path('klem/categorie_article/<int:id>/delete/', Categorie_articleDeleteView.as_view(), name='categorie_article-delete'),
]
urlpatterns += categorie_article_urls + categorie_articleRouteur.urls



# ===========| article urls |========================
from .klemViews.articleViews import ArticleCreateView, ArticleListView, ArticleUpdateView, ArticleDeleteView

articleRouteur = DefaultRouter()
# articleRouteur.register('article_rest', articleViewset, basename='article_viewset' )
article_urls = [
    path('klem/article/new/', ArticleCreateView.as_view(), name='article-create'),
    path('klem/article/list/', ArticleListView.as_view(), name='article-list'),
    path('klem/article/<int:id>/', ArticleUpdateView.as_view(), name='article-update'),
    path('klem/article/<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]
urlpatterns += article_urls + articleRouteur.urls



# ===========| article_tag urls |========================
from .klemViews.article_tagViews import Article_tagCreateView, Article_tagListView, Article_tagUpdateView, Article_tagDeleteView

article_tagRouteur = DefaultRouter()
# article_tagRouteur.register('article_tag_rest', article_tagViewset, basename='article_tag_viewset' )
article_tag_urls = [
    path('klem/article_tag/new/', Article_tagCreateView.as_view(), name='article_tag-create'),
    path('klem/article_tag/list/', Article_tagListView.as_view(), name='article_tag-list'),
    path('klem/article_tag/<int:id>/', Article_tagUpdateView.as_view(), name='article_tag-update'),
    path('klem/article_tag/<int:id>/delete/', Article_tagDeleteView.as_view(), name='article_tag-delete'),
]
urlpatterns += article_tag_urls + article_tagRouteur.urls
