const db = require('./db');

/*db.serialize(() => {
  db.each('SELECT * FROM klemapp_vetement', (err, row) => {
    if (err) {
      console.error('Erreur lors de la requête:', err.message);
    } else {
      console.log(row);
    }
  });
});*/

// Fermer la connexion lorsque tu as terminé
function closeDB(db) {
    db.close((err) => {
        if (err) {
          console.error('Erreur lors de la fermeture de la connexion:', err.message);
        } else {
          console.log('Connexion à SQLite3 fermée');
        }
      });
}

module.exports = { db,closeDB }