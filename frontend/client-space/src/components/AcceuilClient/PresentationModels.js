import React, {useEffect, useState} from 'react';
import '../presentationModels.css'
import { NavLink } from 'react-router-dom';
import ItemModels from './itemModels';

const PresentationModels = () => {

    let itemList1 = [
        {
            image: './img/models/boubou-.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000

        },
        {
            image: './img/models/boubou-.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000

        },
        {
            image: './img/models/boubou2.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000

        },
        {
            image: './img/models/boubou3.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000

        },
        {
            image: './img/models/boubou4.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000

        }
    ]

    let itemList2 = [
        {
            image: './img/models/kaftan.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000
        },
        {
            image: './img/models/kaftan1.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000
        },
        {
            image: './img/models/kaftan2.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000
        },
        {
            image: './img/models/kaftan3.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000
        },
        {
            image: './img/models/kaftan4.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000
        }
    ]

    let itemList3 = [
        {
            image: './img/models/costume.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000
        },
        {
            image: './img/models/costume1.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000
        },
        {
            image: './img/models/costume2.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000
        },
        {
            image: './img/models/costume3.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000
        },
        {
            image: './img/models/costume4.jpg',
            categorie: 'boubou',
            nom: 'boubou',
            type: 'Vêtement pour Hommes',
            price: 5000
        }
    ]

    useEffect(()=>{
        let scroll1 = document.querySelector('.scroll-button1')
        let scroll2 = document.querySelector('.scroll-button2')
        let scroll3 = document.querySelector('.scroll-button3')
        
        let backBtn1 = scroll1.firstElementChild
        let nextBtn1 = scroll1.lastElementChild
        let slider1 = document.querySelector('.boubous .scroll')

        let backBtn2 = scroll2.firstElementChild
        let nextBtn2 = scroll2.lastElementChild
        let slider2 = document.querySelector('.kaftan .scroll')

        let backBtn3 = scroll3.firstElementChild
        let nextBtn3 = scroll3.lastElementChild
        let slider3 = document.querySelector('.tailleurs .scroll')


        let scroll = document.querySelectorAll('.scroll')
        scroll.forEach(element => {
            element.addEventListener('wheel',(event)=>{
                if (event.deltaY !== 0) {
                    window.scrollY += event.deltaY
                }
                else{
                    event.preventDefault()
                    element.scrollLeft += event.deltaX
                    element.style.scrollBehavior = 'smooth'
                }
            })  
       });

        backBtn1.addEventListener('click',()=>{
            slider1.style.scrollBehavior = 'smooth'
            slider1.scrollLeft -= 280
        })
        nextBtn1.addEventListener('click',()=>{
            slider1.style.scrollBehavior = 'smooth'
            slider1.scrollLeft += 280
        })

        backBtn2.addEventListener('click',()=>{
            slider2.style.scrollBehavior = 'smooth'
            slider2.scrollLeft -= 280
        })
        nextBtn2.addEventListener('click',()=>{
            slider2.style.scrollBehavior = 'smooth'
            slider2.scrollLeft += 280
        })

        backBtn3.addEventListener('click',()=>{
            slider3.style.scrollBehavior = 'smooth'
            slider3.scrollLeft -= 280
        })
        nextBtn3.addEventListener('click',()=>{
            slider3.style.scrollBehavior = 'smooth'
            slider3.scrollLeft += 280
        })

    })


    return (
        <div className='models'>
            <div className="title" >
                    <h2>Explorez nos créations</h2>
                    <p>Découvrez votre style en visitant nos modèles uniques !</p>
               </div>
               <div className="sections">
                    <div className="styles-africains">
                        <section className="boubous">
                            <h3>Modèles en <span>Boubou</span></h3>

                            <div className="scroll">
                                <div className="images">
                                    {itemList1
                                        .map((item, index)=>(
                                            <ItemModels key={index} item={item} />
                                        ))
                                    }
                                </div>
                            </div>

                            <div className="scroll-button scroll-button1">
                                <button className='scroll1'>
                                    <img src="./img/icons/previous.ico" alt="prev" />
                                </button>
                                <button className='scroll2'>
                                    <img src="./img/icons/next.ico" alt="next" />
                                </button>
                            </div>
                            <span className="autres"> 
                                <NavLink to='#'>VOIR PLUS</NavLink>    
                            </span>
                        </section>
                    
                        <section className='kaftan'>
                            <h3>Modèles en <span>Kaftan</span></h3>
                            
                            <div className="scroll">
                                <div className="images">
                                    {itemList2
                                        .map((item, index)=>(
                                            <ItemModels key={index} item={item} />
                                        ))
                                    }
                                </div>
                            </div>

                            <div className="scroll-button scroll-button2">
                                <button className='scroll1'>
                                    <img src="./img/icons/previous.ico" alt="prev" />
                                </button>
                                <button className='scroll2'>
                                    <img src="./img/icons/next.ico" alt="next" />
                                </button>
                            </div>
                            <span className="autres"> 
                                <NavLink to='#'>VOIR PLUS</NavLink>    
                            </span>
                        </section>
                    </div>

                    <div className="styles-du-monde">
                        <section className="tailleurs">
                            <h3> Vêtements tailleurs </h3>

                            <div className="scroll">
                                <div className="images slider" >
                                    {itemList3
                                        .map((item, index)=>(
                                            <ItemModels key={index} item={item} />
                                        ))
                                    }
                                </div>
                            </div>

                            <div className="scroll-button scroll-button3">
                                <button className='scroll1'>
                                    <img src="./img/icons/previous.ico" alt="prev" />
                                </button>
                                <button className='scroll2'>
                                    <img src="./img/icons/next.ico" alt="next" />
                                </button>
                            </div>
                            <span className="autres"> 
                                <NavLink to='#'>VOIR PLUS</NavLink>    
                            </span>
                        </section>
                    </div>
               </div>
        </div>
    );
};

export default PresentationModels;