import React from 'react';

const ItemModels = (props) => {
    return (
        <div>
            <figure className='item'>
                <img src={props.item.image} alt={props.item.categorie} />
                <figcaption>
                    <p className="nom">{props.item.nom}</p>
                    <p className="type">{props.item.type}</p>
                    <p className="prix">
                        <span className="value">{props.item.price}</span>
                        <span className="monnaie">$</span>
                    </p>
                </figcaption>
            </figure>
        </div>
    );
};

export default ItemModels;