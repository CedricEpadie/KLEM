import React from 'react';
import { NavLink } from 'react-router-dom';
import '../../assets/css/header.css'
import NavBar from '../NavBar';


const HeaderAcceuil = () => {
    return (
        <div className='header'>
            < NavBar/>
            <div className="next-head">
                <h2>
                    <span>KLEM</span>, l’élégance africaine pour vivre votre histoire
                </h2>
                <div className="link">
                    <NavLink to='/client-creer'>
                            <li>Créer un vêtement</li>
                    </NavLink>
                    <NavLink to='client-models'>
                            <li>Models</li>
                    </NavLink>
                </div>
            </div>

        </div>
    );
};

export default HeaderAcceuil;