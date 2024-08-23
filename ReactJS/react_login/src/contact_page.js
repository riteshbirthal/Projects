import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import cover_5 from "./images/cover-5.jpg";

const Contact_Page = (props) => {
    return (
    <>
        <h1>This is Contact Page.</h1>
        <section class="py-10 py-md-14 overlay overlay-black overlay-60 bg-cover" style={{backgroundImage: "./cover-5.jpg"}}>
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-12 col-md-10 col-lg-8 text-center">
                        <h1 class="display-2 fw-bold text-white">
                            We’re Here to Help.
                        </h1>
                        <p class="lead text-white text-opacity-75 mb-0">
                            We always want to hear from you! Let us know how we can best help you and we'll do our very best.
                        </p>
                    </div>
                </div>
            </div>
        </section>
    </>);
};

export default Contact_Page;