const express = require('express')
const bodyParser = require('body-parser')
const morgan = require("morgan")
const cors = require("cors")

const app = express()
const PORT = 3010

app
    .use(bodyParser.json())
    .use(express.urlencoded({ extended:true }))
    .use(morgan('dev'))
    .use(cors());

require('./getVetement')(app)
require("./getVetementByGender")(app)

app.get("/",(req,res)=>{
    res.json('Hello depuis le BACKEND')
})


app.use(({res})=>{
    const message = "Impossible de trouver la ressource demandee. Veuillez saisir une autre URL."
    res.status(404).json({message})
})

app.listen(PORT,()=>{
    console.log(`L'application demarre sur le port ${PORT}`);
    
})