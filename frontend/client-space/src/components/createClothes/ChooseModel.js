import React from 'react';
import '../../assets/css/chooseModel.css'

const ChooseModel = () => {
    return (
        <div className='chooseModel'>
            <header>
                <h1>
                    <span>1-</span>
                    <span>Choix du modèle</span>
                </h1>
                <h5>Procédons premièrement par le choix votre modèle</h5>    
            </header>
            <section className='choose'>
                    <div className="vues">
                        <button>
                            <img src="./img/icons/upload.svg" alt="upload" />
                        </button>
                    </div>
                    <div className="vues">
                        <button>
                            <img src="./img/icons/upload.svg" alt="upload" />
                        </button>
                    </div>
            </section>
            <button className="next" id='button-next'>Étape suivante</button>
        </div>
    );
};

export default ChooseModel;