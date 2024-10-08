import React from 'react';
import '../../assets/css/chooseCouleur.css'


const ChooseCouleur = () => {
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
                    <textarea name="description" id="description" cols="60" rows="10" placeholder='Description' maxLength={500}></textarea>
                </div>
            </div>
            <button className='terminer'>Terminer</button>
        </div>
    );
};

export default ChooseCouleur;