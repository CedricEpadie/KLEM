import React from 'react';
import '../assets/css/navbar.css'
import { NavLink } from 'react-router-dom';

const NavBar = () => {
    return (
        <div className='navbar'>
            <nav>
                <NavLink to='/client' className='logo'>
                    <img src="./img/logo.png" alt="KLEM" />
                </NavLink>
                <ul>
                    <NavLink to='/createClothes' className={(nav) => (nav.isActive ? 'nav-active' : '')}>
                        <li>Créer un vêtement</li>
                    </NavLink>
                    <NavLink to='client-blog'>
                        <li>
                            Models/categories
                        </li>
                    </NavLink>
                    <a href='/client#client-activite' behavior="smooth">
                        <li>Mon activité</li>
                    </a>
                </ul>

                <div className="notify-account" >
                    <NavLink to='/client-notifications' title="Notifications">
                        <img src="./img/icons/notification.ico" alt="notification" />
                    </NavLink>
                    <button to='/client-account' title="Mon compte">
                        <img src="./img/icons/user.png" alt="user-account" />
                    </button>
                </div>
            </nav>

        </div>
    );
};

export default NavBar;