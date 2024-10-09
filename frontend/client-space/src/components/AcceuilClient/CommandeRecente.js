import React from 'react';
import '../../assets/css/commandeRecente.css'


const CommendeRecente = () => {
    return (
        <div className='containt'>
            <section className="commande-recentes" id='client-activite'>
                <h2>
                    Vos commandes récentes
                </h2>
                <div className="commandes">
                    <div className="vide">
                        AUCUNE COMMANDE RÉCENTE TROUVÉE...
                    </div>
                    <div className="figures">
                        <figure>            
                            <img src="./img/models/boubou-.jpg" alt="vêtement en boubou" />
                            <p className='details-client'>
                                Lorem ipsum dolor sit amet consectetur 
                                adipisicing elit. Numquam, maiores odio 
                                dolorum explicabo, eligendi veniam perspiciatis 
                                itaque, quos soluta cumque qui fugiat eaque nisi 
                                molestias dicta! Consectetur, dignissimos perspiciatis. 
                                Velit?
                            </p>
                            <p className='details'>
                                <p className="Montant">
                                    <span className='descript'>Montant: </span>
                                    <span className='prix'>
                                        <span>5000</span>
                                        <span>FCFA</span>
                                    </span>
                                </p>
                                <p className="qte">
                                    <span className='descript'>Qte: </span><span>5</span>
                                </p>
                                <p className="adress">
                                    <span className='descript'>Adresse: </span><span>550-Rue Du pont</span>
                                </p>
                                <p className='date-lvrs'>
                                    <span className='descript'>Date de livraison: </span>
                                    <span>12 Juillet 2006</span>
                                </p>
                            </p>       
                        </figure>                        
                    </div>
                </div>
            </section>
        </div>
    );
};

export default CommendeRecente;