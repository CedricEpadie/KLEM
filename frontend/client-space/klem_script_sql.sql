-- Active: 1714042484431@@127.0.0.1@5432@klemdb@klemschema


CREATE TABLE IF NOT EXISTS Commentaire(
    idCommentaire INTEGER PRIMARY KEY
);

ALTER TABLE commentaire
ADD COLUMN IF NOT EXISTS idutilisateur INTEGER REFERENCES utilisateur (idutilisateur),
ADD COLUMN IF NOT EXISTS idarticle INTEGER REFERENCES article (idarticle);

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Utilisateur(
    idUtilisateur INTEGER PRIMARY KEY
);

ALTER TABLE utilisateur
ADD COLUMN IF NOT EXISTS idpays INTEGER REFERENCES pays (idpays)

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Pays(
    idPays INTEGER PRIMARY KEY
);


-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Ville(
    idVille INTEGER PRIMARY KEY
);

ALTER TABLE ville
ADD COLUMN IF NOT EXISTS idville INTEGER REFERENCES ville (idville);

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Client(
    idClient INTEGER PRIMARY KEY
);

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Couturier(
    idCouturier INTEGER PRIMARY KEY
);

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Categorie(
    idCategorie INTEGER PRIMARY KEY
);

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Souscription(
    idSouscription INTEGER PRIMARY KEY
);

ALTER TABLE souscription
ADD COLUMN IF NOT EXISTS idcouturier INTEGER REFERENCES couturier (idcouturier),
ADD COLUMN IF NOT EXISTS idabonnement INTEGER REFERENCES abonnement (idabonnement),
ADD COLUMN IF NOT EXISTS date_debut DATE; 

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Commande(
    idCommande INTEGER PRIMARY KEY
);

ALTER TABLE commande
ADD COLUMN IF NOT EXISTS idclient INTEGER REFERENCES client (idclient),
ADD COLUMN IF NOT EXISTS idadmin INTEGER REFERENCES admin (idadmin);

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Vetement(
    idVetement INTEGER PRIMARY KEY
);

ALTER TABLE vetement
ADD COLUMN IF NOT EXISTS idcouturier INTEGER REFERENCES couturier (idcouturier);

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Abonnement(
    idAbonnement INTEGER PRIMARY KEY
);

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Vetement_Commande(
    idVetement_Commande INTEGER PRIMARY KEY
);

ALTER TABLE vetement_commande
ADD COLUMN IF NOT EXISTS idcommande INTEGER REFERENCES commande (idcommande),
ADD COLUMN IF NOT EXISTS idvetement INTEGER REFERENCES vetement (idvetement),
ADD COLUMN IF NOT EXISTS datecommande DATE;

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Admin(
    idAdmin INTEGER PRIMARY KEY
);

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Devis(
    idDevis INTEGER PRIMARY KEY
);

ALTER TABLE devis
ADD COLUMN IF NOT EXISTS idadmin INTEGER REFERENCES admin (idadmin),
ADD COLUMN IF NOT EXISTS idcouturier INTEGER REFERENCES couturier (idcouturier),
ADD COLUMN IF NOT EXISTS idcommande INTEGER REFERENCES commande (idcommande);

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Article(
    idArticle INTEGER PRIMARY KEY
);

ALTER TABLE article
ADD COLUMN IF NOT EXISTS idadmin INTEGER REFERENCES admin (idadmin),
ADD COLUMN IF NOT EXISTS idcategorie INTEGER REFERENCES categorie (idcategorie);

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Tag(
    idTag INTEGER PRIMARY KEY
);

-- #########-----------------------------------------------##############------------

CREATE TABLE IF NOT EXISTS Article_Tag(
    idArticle_Tag INTEGER PRIMARY KEY
);

ALTER TABLE article_tag
ADD COLUMN IF NOT EXISTS idarticle INTEGER REFERENCES article (idarticle),
ADD COLUMN IF NOT EXISTS idtag INTEGER REFERENCES tag (idtag),
ADD COLUMN IF NOT EXISTS date DATE;

