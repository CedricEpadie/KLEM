import React, { useEffect, useState } from 'react';
import '../assets/css/createClothes.css'
import NavBar from '../components/NavBar';
import PopUpProfil from '../components/PopUpProfil';
import ChooseModel from '../components/createClothes/ChooseModel';
import ChooseCouleur from '../components/createClothes/ChooseCouleur';

const CreateClothes = () => {
    

    useEffect(()=>{
        let navbar = document.querySelector(".navbar nav")
        navbar.classList.add("createClothe")
        /* --------------------------------------------------------------- */
        let profilBtn = document.querySelector('.notify-account button')
        let profilPopUp = document.querySelector('.popUpProfil')
        profilBtn.addEventListener('click',()=>{
            profilPopUp.classList.remove('leaveStyle')
        })
        /* -------------------------------------------------------------- */

        let uplodImage = document.querySelectorAll('.upload')
        let popUpSelect = document.querySelector(".popUpSelect")
        let popUpSelectCloseButton = document.querySelector(".popUpSelect ._cancel img")

        uplodImage.forEach(button => {
            button.addEventListener("click",()=>{
                popUpSelect.classList.remove("unselect")
                chooseImage()
            })
        })
        popUpSelectCloseButton.addEventListener("click",()=>{
            popUpSelect.classList.add("unselect")
        })

        /* ------------------------------------------------------------- */



    })


    return (
        <div className='createClothes'>
            < NavBar/>
            < PopUpProfil/>
            <div className="creationSpace">
                <div className="chooses">
                   <div className="choose-container">
                        <div className="images">
                            <div className="vues">
                            <img src="./img/models/boubou2.jpg" alt="" />
                            </div>
                            <div className="vues">
                            <img src="./img/models/boubou2.jpg" alt="" />
                            </div>
                        </div>
                        <div className="game-color">
                            <h3>Teintes et  couleur</h3>
                            <div className="color">
                                <div></div>
                                <div></div>
                                <div></div>
                            </div>    
                        </div>
                        <div className="choose-description">
                            <h3>Détails de la commande:</h3>
                            <p>
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                                Laudantium consequuntur aut nihil soluta illum dignissimos rem. 
                                Corrupti expedita, fugit aperiam repudiandae eligendi maiores 
                                rem necessitatibus. Lorem, ipsum dolor sit amet consectetur 
                                adipisicing elit. Molestias, rem!
                            </p>
                        </div>
                   </div>
                   <div className="send">
                        <button>Commander</button>
                   </div>
                </div>
                {/*< ChooseCouleur/>*/}
                <ChooseModel/>
                <div className="popUpSelect unselect">
                    <div className="_cancel">
                        <img src="./img/icons/_cancel.ico" alt="cancel" />
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
                            <img src="./img/models/boubou.jpg" alt="vetement" className='model'/>
                            <figcaption>
                                <img src="./img/icons/upload.svg" alt="upload" />                            
                            </figcaption>
                        </figure>
                        
                    </div>
                    <div className='button'>
                        <button className='validate'>Valider</button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default CreateClothes;


function chooseImage(){

    let listImages = document.querySelectorAll(".vetements figure")
    let chooseContainerImages = document.querySelector(".choose-container .images")


    console.log(chooseContainerImages)

    listImages.forEach(image =>{
        image.lastElementChild.addEventListener("click",()=>{
            console.log(image)
        })
    })


}