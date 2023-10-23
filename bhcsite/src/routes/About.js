import React from 'react';
import "./styles/AboutStyles.css";
import Navbar from '../components/Navbar';
import Footer from "../components/Footer";

const About = () => {
  return (
    <div className="about-page" >
    <Navbar />
    <div className='about-page-container'>
      <h1>About Page</h1>
      <p>This page is still being developed.</p>
      </div>
    <Footer />
    </div>
  )
}

export default About
