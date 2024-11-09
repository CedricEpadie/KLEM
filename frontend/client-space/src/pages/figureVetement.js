import React from 'react';

const FigureVetement = (props) => {
    return (
        <figure>
            <img src={"./img/models/" + props.client.image} alt="vetement" className='model' id={props.client.id}/>
            <figcaption>
                <img src="./img/icons/upload.svg" alt="upload" />                            
            </figcaption>
        </figure>
    );
};

export default FigureVetement;