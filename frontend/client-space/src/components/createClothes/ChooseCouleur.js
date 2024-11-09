import React, { useEffect } from 'react';
import '../chooseCouleur.css'


const ChooseCouleur = () => {

    useEffect(()=>{
        /* Button de commande */
        let commandeButton = document.querySelector(".send button")
        let selectSpace = document.querySelector(".chooses")

        let validateButton = document.querySelector(".terminer")
        let gameCouleurs = document.querySelectorAll("input[type='color']")
        let description = document.querySelector('#description')
        let chooseList = document.querySelector('.choose-container')

        validateButton.addEventListener('click',()=>{
            chooseList.firstElementChild.nextElementSibling.innerHTML = `
                            <h3>Teintes et couleur</h3>
                            <div class = "color">
                                <div></div>
                                <div></div>
                                <div></div>
                            </div>
                        `
            chooseList.lastElementChild.innerHTML = `
                                <h3>Détails de la commande:</h3>
                            <p>
                                ${description.value}
                            </p>
                        `
            
            setTimeout(() => {
                let couleurs = document.querySelectorAll('.game-color .color div')
                couleurs[0].style.backgroundColor = gameCouleurs[0].value
                couleurs[1].style.backgroundColor = gameCouleurs[1].value
                couleurs[2].style.backgroundColor = gameCouleurs[2].value
            }, 250);

            setTimeout(() => {
                gameCouleurs[0].value = "#dcdcdc"
                gameCouleurs[1].value = "#dcdcdc"
                gameCouleurs[2].value = "#dcdcdc"
                description.value = ""
            }, 750);
            
            setTimeout(() => {
                commandeButton.classList.remove("wait")
                selectSpace.scrollTop = 1000
            }, 1000);            

        })
        

    })


    return (
        <div className='chooseCouleur'>
            <h1>Choix des couleurs
                et description details
            </h1>
            <div className="color-description">
                <div>
                    <h3>Game de couleurs</h3>
                    <div>
                        <input type="color" name="color1" id="color1" defaultValue={"#dcdcdc"}/>
                        <input type="color" name="color2" id="color2" defaultValue={"#dcdcdc"}/>
                        <input type="color" name="color3" id="color3" defaultValue={"#dcdcdc"}/>    
                    </div>  
                </div>
                <div>
                    <textarea 
                        name="description" 
                        id="description" 
                        cols="60" rows="10" 
                        placeholder='Description de la commande(mensuration, taille, matières du tissu, personnalisations personnelles...)' 
                        maxLength={1200}>
                    </textarea>
                </div>
            </div>
            <button className='terminer'>Valider</button>
        </div>
    );
};

export default ChooseCouleur;