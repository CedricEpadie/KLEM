import React from 'react';
import '../../assets/css/mainAcceuil.css'
import { useEffect } from 'react';
import PresentationModels from './PresentationModels';
import CommandeRecente from './CommandeRecente'


const MainAcceuil = () => {

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
                event.preventDefault()
                element.scrollLeft += event.deltaX
                element.style.scrollBehavior = 'smooth'
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
        <div className="main-accueil">
            
            <CommandeRecente/>
            <PresentationModels/>
            
        </div>
    );
};

export default MainAcceuil;