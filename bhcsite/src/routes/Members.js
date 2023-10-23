import React from 'react';
import "./styles/MembersStyles.css";
import Navbar from '../components/Navbar';
import Footer from "../components/Footer";

const Members = () => {
  return (
    <div className="about-page">
    <Navbar />
    <div className='members-page-container'>
      <h1>Certified Members Page</h1>
      <p>This page is still being developed.</p>
    </div>
    <Footer />
    </div>
  )
}

export default Members
