// AboutSection.js
import React from 'react';
import "./styles/CertifiedMembersSectionStyles.css"
import { Link } from 'react-router-dom';


const CertifiedMembersSection = () => {
  
  return (
    <div className="section-container" >
        <div className='certified-members-section'>
      <div className="certifed-section-text">
        <h2 className="section-title">Certified Members</h2>
        <p>These companies/businesses have undergone a rigorous Halal auditing process and qualified for BHC-GH's Halal certification. This means they offer Halal products and services, and do not mix their services with anything that isn't Halal.</p>
        
        <small className="for-large-screen">
            <Link to={"/members"} className="more-link link-certified">See all certified members</Link>
        </small>
      </div>
      <div className="certified-members">
        <div className="certified-member-card">
            <div className="business-logo">logo</div>
            <h4>Business Name</h4>
            <small>Business Location Details</small>
        </div>
        <div className="certified-member-card">
            <div className="business-logo">logo</div>
            <h4>Business Name</h4>
            <small>Business Location Details</small>
        </div>
        <div className="certified-member-card">
            <div className="business-logo">logo</div>
            <h4>Business Name</h4>
            <small>Business Location Details</small>
        </div>
      </div>
      <small className="for-small-screen">
            <Link to={"/members"} className="more-link link-certified">See all certified members</Link>
        </small>
        </div>
    </div>
  );
};

export default CertifiedMembersSection;