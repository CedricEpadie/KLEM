const sqlite3 = require('sqlite3').verbose();

// Ouvrir la connexion à la base de données (ou la créer si elle n'existe pas)
const db = new sqlite3.Database('./db.sqlite3', (err) => {
    if (err) {
      console.error('Erreur lors de l\'ouverture de la base de données:', err.message);
    } else {
      console.log('Connecté à la base de données SQLite3');
    }
  });
  
module.exports = db;