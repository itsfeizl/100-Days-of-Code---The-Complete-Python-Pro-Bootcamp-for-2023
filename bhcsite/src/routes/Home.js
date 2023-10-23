import React from 'react'
import Navbar from '../components/Navbar';
import Footer from "../components/Footer"
import "./styles/HomeStyles.css";
import SliderComponent from '../components/Slider';
import NewsSection from '../components/NewsSection';
import AboutSection from '../components/AboutSection';
import MissionVision from '../components/MissionVision';
import ServicesSection from '../components/ServicesSection';
import CertifiedMembersSection from '../components/CertifiedMembersSection';
import BecomeAMemberSection from '../components/BecomeAMemberSection';

const Home = () => {

  const slides = [
    {
      title: "<h2>A trustworthy source for halal Excellence<h2>",
      description: "<p>BHC GHANA is a Halal <span>auditing</span>, <span>training</span>, and <span>certification</span> body that promotes higher and inclusive Halal standards to meet the dietary preferences of the Ghanaian people.<p>"
    },
    {
      title: "<h2>Halal standards tailored to every industry</h2>",
      description: "<p>Description</p>"
    },
    {
      title: "<h2>Ensuring High and Authentic Halal standards<h2>",
      description: "<p>Description to CAPTION 2</p>"
    },
    {
      title: "<h2>Join the Course to Upholding Halal Integrity<h2>",
      description: "<p>Description to CAPTION 3</p>"
    },
  ];


  return (
    <div className="homepage">
        <Navbar />
        <SliderComponent slides={slides} />
        <NewsSection />
        <AboutSection />
        <MissionVision />
        <ServicesSection />
        <CertifiedMembersSection />
        <BecomeAMemberSection />
        <div style={{ height: "600px"}}></div>
        <Footer />
    </div>
  )
}

export default Home
