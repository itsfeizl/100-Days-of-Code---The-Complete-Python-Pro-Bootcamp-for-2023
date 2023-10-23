// Slider.js
import React, { useState, useRef } from 'react';
import "./styles/Slider.css";
import backgroundImage from '../components/assets/background.png';
import { NavLink } from 'react-router-dom';
import Slider from 'react-slick';

import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

const SliderComponent = ({ slides }) => {
  const [autoplay, setAutoplay] = useState(true);
  const sliderRef = useRef(null);

  const settings = {
    dots: true,
    infinite: true,
    speed: 1000, // Adjust the speed as needed
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: autoplay, // Control autoplay with state
    autoplaySpeed: 3000, // Set the autoplay interval (e.g., 3 seconds)
    beforeChange: (currentSlide, nextSlide) => {
      // Stop autoplay when manually navigating
      setAutoplay(true);
    }
  };

  const containerStyle = {
    backgroundImage: `url(${backgroundImage})`,
    backgroundRepeat: 'no-repeat'
  };

  return (
    <div className="slider-container" style={containerStyle}>
      <Slider {...settings} ref={sliderRef} className="slider">
        {slides.map((slide, index) => (
          <div key={index} className="slide">
            {/* Render title and description with HTML tags */}
            <div dangerouslySetInnerHTML={{ __html: slide.title }}></div>
            <div dangerouslySetInnerHTML={{ __html: slide.description }}></div>
          </div>
        ))}
      </Slider>
      <div className="start-application">
        <NavLink to="/join" style={{display: "flex"}} className="apply-support-link">
          <div className="start-application-link">
            Start Application
          </div>
        </NavLink>
        <NavLink to="/donate" style={{display: "flex"}} className="apply-support-link">
          <div className="start-application-link support-us">
            Support Us
          </div>
        </NavLink>
      </div>
    </div>
  );
};

export default SliderComponent;
