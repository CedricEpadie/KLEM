import React from 'react';
import '../../assets/css/mainAcceuil.css'
import PresentationModels from './PresentationModels';
import CommandeRecente from './CommandeRecente'


const MainAcceuil = () => {

    return (
        <div className="main-accueil">
            
            <CommandeRecente/>
            <PresentationModels/>
            
        </div>
    );
};

export default MainAcceuil;