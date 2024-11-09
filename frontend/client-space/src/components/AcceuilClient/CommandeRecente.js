import React from 'react';
import '../commandeRecente.css'
import FigureCommandeRecente from './FigureCommandeRecente';

const CommendeRecente = () => {

    let figure = [
        {
            img :  "bg.jpeg",
            details :   "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sit est soluta repudiandae  doloribus perferendis vitae beatae vel, deleniti                     optio, ab necessitatibus voluptatem obcaecati tempora ex!",
            montant:  5000,
            qte:  18,
            adress:  "75 Rue du Pont",
            dateLivraison:  '24-04-2007' 
        },
        {
            img :  "bg.jpeg",
            details :   "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sit est soluta repudiandae  doloribus perferendis vitae beatae vel, deleniti                     optio, ab necessitatibus voluptatem obcaecati tempora ex!",
            montant:  10000,
            qte:  2,
            adress:  "78 Rue la cité",
            dateLivraison:  '24-04-2010' 
        }
    ]

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
                        {figure
                        .map((commande, index)=>(
                            <FigureCommandeRecente 
                                key={index} commande={commande}
                            />
                        ))

                        }
                    </div>
                </div>
            </section>
        </div>
    );
};

export default CommendeRecente;