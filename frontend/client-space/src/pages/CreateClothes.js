import React, { useEffect, useState } from 'react';
import './createClothes.css'
import NavBar from '../components/NavBar';
import PopUpProfil from '../components/PopUpProfil';
import ChooseModel from '../components/createClothes/ChooseModel';
import ChooseCouleur from '../components/createClothes/ChooseCouleur';
import FigureVetement from './figureVetement';
import axios from "axios"

const CreateClothes = () => {
    const [choose, setChoose] = useState(<ChooseModel/>)
    const [datas, setDatas] = useState([])

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

        //Requête de récupération des images depuis l'API
        axios.get("http://localhost:3010/api/vetements")
        .then((res) => setDatas(res.data));

        //Gestion de l'affichage de chaque image par catégorie
        let contentClothes = document.querySelector(".vetements")
        let categories =  document.querySelectorAll(".genre input[type='radio']")
        categories.forEach(categorie=>{
            categorie.addEventListener("click",()=>{
                contentClothes.innerHTML = ''
                datas.forEach(client=>{
                    if (client.genre === categorie.id) {
                        let figure = document.createElement("figure")
                            figure.innerHTML = `
                                <img src="./img/models/${client.image}" alt="vetement" class='model' id=${client.id}/>
                                <figcaption>
                                    <img src="./img/icons/upload.svg" alt="upload" />                            
                                </figcaption>
                            `
                        contentClothes.appendChild(figure)
                    }
                })   
            })
        })


    },[])
  

    return (
        <div className='createClothes'>
            < NavBar/>
            < PopUpProfil/>
            <div className="creationSpace">
                <div className="chooses">
                   <div className="choose-container">
                        <div className="images">
                        </div>
                        <div className = "game-color">
                        </div>
                        <div className = "choose-description">
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
                            <input type="radio" name="choix" id="masculin" />
                        </span>
                        <span>
                            <label htmlFor="choix">Femme</label>
                            <input type="radio" name="choix" id="feminin" />
                        </span>
                    </div>
                    <div className="vetements">  
                        {datas
                            .map((client, index)=>(
                                <FigureVetement key={index} client={client} />
                            ))
                        }                      
                    </div>
                    
                </div>
            </div>
        </div>
    );
};

export default CreateClothes;
