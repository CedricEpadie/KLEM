import React, { useEffect } from 'react';
import { NavLink } from 'react-router-dom'
import '../assets/css/popUpProfil.css'


const PopUpProfil = () => {

    useEffect(() =>{
        let popUpProfil = document.querySelector('.popUpProfil')
        let popUpButton = document.querySelector('.popUpProfil .user .leave') 
        
        popUpButton.onclick = ()=>{
            popUpProfil.classList.add('leaveStyle')
        }

    }) 

    return (
        <div className='popUpProfil leaveStyle'>
            <div className="user">
                <div>
                    <img src="./img/icons/user.png" alt="userImage" />
                    <span className="infos">
                        <p>Username</p>
                        <p>Name of the user</p>
                    </span>
                </div>
                <img src="./img/icons/_cancel.ico" alt="leave" className='leave'/>
            </div>
            <div className="container">
                <li>
                    <NavLink>
                        <img src="./img/icons/account.ico" alt="profil" />
                        <span>Mon profile</span>
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="./img/icons/setting.ico" alt="profil" />
                        <span>Paramètres</span>
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="./img/icons/study.ico" alt="profil" />
                        <span>Mon activité</span>
                    </NavLink>
                </li>
                <li>
                    <NavLink>
                        <img src="./img/icons/_exit.ico" alt="profil" />
                        <span>Se déconnecter</span>
                    </NavLink>
                </li>
            </div>

            { 

            }

        </div>
    );
};

export default PopUpProfil;