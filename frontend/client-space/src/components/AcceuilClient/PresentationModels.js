import React, {useEffect} from 'react';
import '../../assets/css/presentationModels.css'
import { NavLink } from 'react-router-dom';


const PresentationModels = () => {

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

                            <figure className='item'>
                                <img src="./img/models/boubou-.jpg" alt="vêtement en boubou" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>                           

                            <figure className='item'>
                                <img src="./img/models/boubou.jpg" alt="vêtement en boubou" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
                            <figure className='item'>
                                <img src="./img/models/boubou2.jpg" alt="vêtement en boubou" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
                            <figure className='item'>
                                <img src="./img/models/boubou3.jpg" alt="vêtement en boubou" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
                            <figure className='item'>
                                <img src="./img/models/boubou4.jpg" alt="vêtement en boubou" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
                            <figure className='item'>
                                <img src="./img/models/boubou4.jpg" alt="vêtement en boubou" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>

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

                            <figure className='item'>
                                <img src="./img/models/kaftan.jpg" alt="vêtement Kaftan" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
                            <figure className='item'>
                                <img src="./img/models/kaftan1.jpg" alt="vêtement Kaftan" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
                            <figure className='item'>
                                <img src="./img/models/kaftan2.jpg" alt="vêtement Kaftan" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
                            <figure className='item'>
                                <img src="./img/models/kaftan3.jpg" alt="vêtement Kaftan" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
                            <figure className='item'>
                                <img src="./img/models/kaftan4.jpg" alt="vêtement Kaftan" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>

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
                            <figure className='item'>
                                <img src="./img/models/costume.jpg" alt="vêtement tailleur" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
                            <figure className='item'>
                                <img src="./img/models/costume1.jpg" alt="vêtement tailleur" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
                            <figure className='item'>
                                <img src="./img/models/costume2.jpg" alt="vêtement tailleur" />
                                <figcaption><p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
                            <figure className='item'>
                                <img src="./img/models/costume3.jpg" alt="vêtement tailleur" />
                                <figcaption>
                                    <p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
                            <figure className='item'>
                                <img src="./img/models/costume4.jpg" alt="vêtement tailleur" />
                                <figcaption>
                                    <p className="nom">Lorem, ipsum.</p>
                                    <p className="type">Lorem.</p>
                                    <p className="prix">
                                        <span className="value">5000</span><span className="monnaie">$</span>
                                    </p>
                                </figcaption>
                            </figure>
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