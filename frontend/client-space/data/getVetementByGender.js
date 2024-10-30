
let db = require("./function")

module.exports =  (app) =>{
    app.get("/api/vetements/:gender",(req, res) =>{
        let genre = req.params.gender
        
        db.db.serialize(() => {
            db.db.all(`SELECT * FROM klemapp_vetement WHERE genre="${genre}"`,async (err, row) => {
              if (err) {
                console.error('Erreur lors de la requête:', err.message);
              } else {
                setTimeout(() => {
                    res.json(row)
                }, 750);
              }
            });
        });
    })
}
