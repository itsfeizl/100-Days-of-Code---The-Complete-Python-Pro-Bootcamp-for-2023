// AboutSection.js
import React from 'react';
import "./styles/AboutSectionStyles.css";
import image1 from "./assets/placeholder-img.jpg";
import { Link } from 'react-router-dom';


const AboutSection = () => {
  
  return (
    <div className="section-container about-section-container" >
      <div className="about-text">
        <h2 className="about-text-heading">Your Trusted Guardian of Halal Authenticity</h2>
        <p>The BHC-Ghana was incorporated to help ensure and assure that Muslims could be confident the meat and food products they consume are ‘purely Halal’. BHC-Ghana is an independent, non-profit, Ghanaian registered organization which monitors, inspects and certifies Halal products for the benefit of the Muslim community.</p>
        <p>
          <Link to={"/about"} className="more-link">More about us</Link>
        </p>
      </div>
      <div className="board-members">
        <div className="board-members-title">
          <h3>Meet Our Board Members</h3>
          <Link to={"/about"} className="more-link">All Members</Link>
        </div>
        <div className="board-member-cards-container">
        <div className="board-member-card">
            <div className="board-member-img">
              <img className="news-img" src={image1} alt='newsimage'/>
            </div>
            <h4>Dr. Tamim Abdul Wahab</h4>
            <small>Sharia expert and Dean of Islamic studies, University Name</small>
          </div>
          <div className="board-member-card">
            <div className="board-member-img">
              <img className="news-img" src={image1} alt='newsimage'/>
            </div>
            <h4>Prof. Dr Anwar Sahib</h4>
            <small>President, Federation of Muslim Scholars of New Zealand (FMSNZ)</small>
          </div>
          <div className="board-member-card">
            <div className="board-member-img">
              <img className="news-img" src={image1} alt='newsimage'/>
            </div>
            <h4>Sheikh Abdullatif A. Sheikh</h4>
            <small>Board Member, Kenya Bureau of Halal Certification, Nairobi</small>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AboutSection;