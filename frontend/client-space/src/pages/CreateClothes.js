import React, { useEffect, useState } from 'react';
import '../assets/css/createClothes.css'
import NavBar from '../components/NavBar';
import PopUpProfil from '../components/PopUpProfil';
import ChooseModel from '../components/createClothes/ChooseModel';
import ChooseCouleur from '../components/createClothes/ChooseCouleur';

const CreateClothes = () => {
    const [choose, setChoose] = useState(<ChooseModel/>)

    useEffect(()=>{
        let navbar = document.querySelector(".navbar nav")
        navbar.classList.add("createClothe")
        /* --------------------------------------------------------------- */
        let profilBtn = document.querySelector('.notify-account img')
        let profilPopUp = document.querySelector('.popUpProfil')

        profilBtn.addEventListener('click',()=>{
            profilPopUp.classList.remove('leaveStyle')
        })
        /* --------------------------------------------------------------------------- */
            /* Ouverture et fermeture de la PopUp de selection du vêtement */
        let uploadImage = document.querySelectorAll('.choose img')
        let popUpSelect = document.querySelector(".popUpSelect")
        let popUpSelectCloseButton = document.querySelector(".popUpSelect ._cancel img")
        let selectModelButton  = document.querySelector('.select')

        uploadImage.forEach(button => {
            button.addEventListener("click",()=>{
                popUpSelect.classList.remove("unselect")
            })
        })
        selectModelButton.addEventListener("click",()=>{
            popUpSelect.classList.remove("unselect")
        })
        popUpSelectCloseButton.addEventListener("click",()=>{
            popUpSelect.classList.add("unselect")
        })

        let buttonNext1 = document.querySelector("#button-next")
        let buttonList = document.querySelector(".bouttons")

        buttonNext1.addEventListener("click",()=>{
            setTimeout(() => {
                setChoose(<ChooseCouleur/>)
                buttonList.style.display = 'none'
            }, 1500);
        })

    })
  

    return (
        <div className='createClothes'>
            < NavBar/>
            < PopUpProfil/>
            <div className="creationSpace">
                <div className="chooses">
                   <div className="choose-container">
                        <div className="images">
                            {/*<div className="vues">
                                <img src="./img/models/boubou2.jpg" alt="" />
                            </div>
                            <div className="vues">
                                <img src="./img/models/boubou2.jpg" alt="" />
                            </div>*/}
                        </div>
                        <div className="game-color">
                            {/*<h3>Teintes et  couleur</h3>
                            <div className="color">
                                <div></div>
                                <div></div>
                                <div></div>
                            </div>*/}   
                        </div>
                        <div className="choose-description">
                            {/*<h3>Détails de la commande:</h3>
                            <p>
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                                Laudantium consequuntur aut nihil soluta illum dignissimos rem. 
                                Corrupti expedita, fugit aperiam repudiandae eligendi maiores 
                                rem necessitatibus. Lorem, ipsum dolor sit amet consectetur 
                                adipisicing elit. Molestias, rem!
                            </p>*/}
                        </div>
                   </div>
                   <div className="send">
                        <button className='wait'>Commander</button>
                   </div>
                </div>
                {choose}
                <div className="bouttons">
                    <button className='select'>Choisir son model</button>
                    <button className="next unclickable" id='button-next' >Étape suivante</button>
                </div>
                <div className="popUpSelect unselect">
                    <div className="_cancel">
                        <img src="./img/icons/close.svg" alt="cancel" />
                    </div>
                    <h4 className="select-genre">Genre: </h4>
                    <div className="genre">
                        <span>
                            <label htmlFor="choix">Homme</label>
                            <input type="radio" name="choix" id="homme" />
                        </span>
                        <span>
                            <label htmlFor="choix">Femme</label>
                            <input type="radio" name="choix" id="femme" />
                        </span>
                    </div>
                    <h4 className='select-categorie'>Catégorie:</h4>
                    <div className="categories">
                        <div className="cat-hommes cat">
                            <span>
                                <label htmlFor="categories">Boubou</label>
                                <input type="radio" name="categories" id="boubou" />
                            </span>
                            <span>
                                <label htmlFor="categories">Costumes</label>
                                <input type="radio" name="categories" id="costumes" />
                            </span>
                            <span>
                                <label htmlFor="categories">Dashiki</label>
                                <input type="radio" name="categories" id="dashiki" />
                            </span>
                            <span>
                                <label htmlFor="categories">Sport</label>
                                <input type="radio" name="categories" id="sport" />
                            </span>
                        </div>
                        <div className="cat-femmes cat">
                                
                            <span>
                                <label htmlFor="categories">Boubou</label>
                                <input type="radio" name="categories" id="boubou" />
                            </span>
                            <span>
                                <label htmlFor="categories">Costumes</label>
                                <input type="radio" name="categories" id="costumes" />
                            </span>
                            <span>
                                <label htmlFor="categories">Robes</label>
                                <input type="radio" name="categories" id="robes" />
                            </span>
                            <span>
                                <label htmlFor="categories">Sport</label>
                                <input type="radio" name="categories" id="sport" />
                            </span>
                            <span>
                                <label htmlFor="categories">Tenues de mariage</label>
                                <input type="radio" name='categories' id='mariage'/>
                            </span>
                           
                        </div>
                    </div>
                    <div className="vetements">
                        <figure>
                            <img src="./img/models/boubou.jpg" alt="vetement" className='model'/>
                            <figcaption>
                                <img src="./img/icons/upload.svg" alt="upload" />                            
                            </figcaption>
                        </figure>
                        <figure>
                            <img src="./img/models/boubou2.jpg" alt="vetement" className='model'/>
                            <figcaption>
                                <img src="./img/icons/upload.svg" alt="upload" />                            
                            </figcaption>
                        </figure>
                        
                    </div>
                    
                </div>
            </div>
        </div>
    );
};

export default CreateClothes;
