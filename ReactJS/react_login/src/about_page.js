import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import photo_16 from "./images/photo-16.jpg";
import photo_17 from "./images/photo-17.jpg";
import photo_18 from "./images/photo-18.jpg";
import photo_19 from "./images/photo-19.jpg";
import photo_20 from "./images/photo-20.jpg";
import photo_21 from "./images/photo-21.jpg";

const About_Page = (props) => {
    return (
    <>
        <section class="py-8 py-md-11 border-bottom">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-12 col-md-10 col-lg-8 text-center">
                    <h1 class="display-2">
                        Small team. Big hearts.
                    </h1>
                    <p class="lead text-body-secondary mb-7 mb-md-9">
                        Our focus is always on finding the best people to work with. Our bar is high, but you look ready to take on the challenge.
                    </p>

                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <div class="row gx-4">
                        <div class="col-4">
                            <img class="img-fluid rounded shadow-lg" src={photo_16} alt="..."/>
                        </div>
                        <div class="col-3">
                            <img class="img-fluid rounded shadow-lg mb-4" src={photo_17} alt="..."/>
                            <img class="img-fluid rounded shadow-lg" src={photo_18} alt="..."/>
                        </div>
                        <div class="col-5">
                            <div class="row gx-5 mb-4">
                                <div class="col-5">
                                    <img class="img-fluid rounded shadow-lg" src={photo_19} alt="..."/>
                                </div>
                                <div class="col-7">
                                    <img class="img-fluid rounded shadow-lg" src={photo_20} alt="..."/>
                                </div>
                            </div>
                            <img class="img-fluid rounded shadow-lg" src={photo_21} alt="..."/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </section>
    </>);
};

export default About_Page;