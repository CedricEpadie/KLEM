import React from 'react';

const FigureCommandeRecente = (props) => {
    return (
        <div>
            <figure>            
                <img src={"./" + props.commande.img} alt="vêtement en boubou" />
                <p className='details-client'>{props.commande.details}</p>
                <p className='details'>
                    <p className="Montant">
                        <span className='descript'>Montant: </span>
                        <span className='prix'>
                            <span>{props.commande.montant}</span>
                            <span>FCFA</span>
                        </span>
                    </p>
                    <p className="qte">
                        <span className='descript'>Qte: </span><span>{props.commande.qte}</span>
                    </p>
                    <p className="adress">
                        <span className='descript'>Adresse: </span><span>{props.commande.adress}</span>
                    </p>
                    <p className='date-lvrs'>
                       <span className='descript'>Date de livraison: </span>
                       <span>{props.commande.dateLivraison}</span>
                    </p>
                </p>                       
            </figure>
        </div>
    );
};

export default FigureCommandeRecente;