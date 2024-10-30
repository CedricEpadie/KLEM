let db = require("./function")
let vetementList = [];

module.exports =  (app) =>{
    app.get("/api/vetements",(req, res) =>{
        db.db.serialize(() => {
            db.db.all('SELECT * FROM klemapp_vetement',async (err, row) => {
              if (err) {
                console.error('Erreur lors de la requête:', err.message);
              } else {
                setTimeout(() => {
                  res.send(row)
                }, 750);
              }
            });
        });
    })
}

