import React, { useEffect } from 'react';
import '../../assets/css/chooseModel.css'


const ChooseModel = () => {

    useEffect(()=>{
        
        let uploadImage = document.querySelectorAll('.choose img')
        let popUpSelect = document.querySelector(".popUpSelect")

        /* ---------------------------------------------------------------------------------------- */
            /* Choix de l'image et son insertion dans la zone de presentation des models */
            let buttonNext1 = document.querySelector("#button-next")//Bouton pour aller à l'étape suivante
            let figureList = document.querySelectorAll('.vetements figure figcaption img:last-child')// On selectionne toutes les images Upload
            let imageSelected = document.querySelectorAll(".choose .vues")
            setInterval(() => { // Ceci vas nous permettre d'initialiser toutes les 500ms la liste des images
                figureList = document.querySelectorAll('.vetements figure figcaption img:last-child')
            
                figureList.forEach( figure=>{
                    figure.addEventListener('click',()=>{
        
                        imageSelected[0].innerHTML = "" 
                        imageSelected[1].innerHTML = ""
                        let img = document.createElement("img")
                        let divElement = document.createElement("div")
        
                        img.setAttribute("class","choix")
                        img.src = `./img`+figure.parentElement.previousElementSibling.src.split("img")[1]
                        divElement.appendChild(img)
                        
                        imageSelected.innerHTML = ""
                        setTimeout(() => {
                            uploadImage = document.querySelectorAll('.choose img')
                            buttonNext1.classList.remove("unclickable")
                        }, 2000);   
                        imageSelected[0].innerHTML = divElement.innerHTML
                        imageSelected[1].innerHTML = divElement.innerHTML
                        popUpSelect.classList.add("unselect")
        
                    })
                })
            }, 500);
            
            /* --------------------------------------------------------------------------------------- */
                /* Gestion du passage à l'étape suivante */
            let chooseList = document.querySelector('.choose-container')
            let vue1 = document.createElement("div")
            vue1.setAttribute("class","vues")
            let vue2 = document.createElement("div")
            vue2.setAttribute("class","vues")
            buttonNext1.addEventListener('click',(event)=>{
                event.preventDefault()
                vue1.innerHTML = imageSelected[0].innerHTML
                vue2.innerHTML = imageSelected[1].innerHTML
    
                chooseList.firstElementChild.appendChild(vue1)
                chooseList.firstElementChild.appendChild(vue2)
    
                setTimeout(() => {
                    imageSelected[0].innerHTML = `<button>
                                <img src="./img/icons/image.svg" alt="image" className='upload'/>
                            </button>`
                    imageSelected[1].innerHTML = `<button>
                                <img src="./img/icons/image.svg" alt="image" className='upload'/>
                            </button>`
                }, 1500);
                
                setTimeout(() => {
                    while (chooseList.firstElementChild.childNodes.length !== 2) {
                        chooseList.firstElementChild.removeChild(chooseList.firstElementChild.lastElementChild)
                    }
                }, 1000);
                
            })

    })


    return (
        <div className='chooseModel'>
            <header>
                <h1>
                    <span>1-</span>
                    <span>Choix du modèle</span>
                </h1>
                <h5>Procédons premièrement par le choix votre modèle</h5>    
            </header>
            <section className='choose'>
                    <div className="vues">
                        <button>
                            <img src="./img/icons/image.svg" alt="image" className='upload'/>
                        </button>
                    </div>
                    <div className="vues">
                        {/*<img src="./img/models/boubou2.jpg" alt="models" className='choix'/>*/}
                        <button>
                            <img src="./img/icons/image.svg" alt="image" className='upload'/>
                        </button>
                    </div>
            </section>
            
        </div>
    );
};

export default ChooseModel;