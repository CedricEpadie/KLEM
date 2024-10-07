import React from 'react';
import MainAcceuil from '../components/AcceuilClient/MainAcceuil';
import HeaderAcceuil from '../components/AcceuilClient/HeaderAcceuil';
import PopUpProfil from '../components/PopUpProfil';
import { useEffect } from 'react';

const AcceuilClient = () => {
    
    useEffect(()=>{

        let profilBtn = document.querySelector('.header .notify-account button')
        let profilPopUp = document.querySelector('.popUpProfil')

        profilBtn.addEventListener('click',()=>{
            profilPopUp.classList.remove('leaveStyle')
        })
    })


    return (
        <div className='acceuil-client'>
            <PopUpProfil />
            <HeaderAcceuil />
            <MainAcceuil />
        </div>
    );
};

export default AcceuilClient;