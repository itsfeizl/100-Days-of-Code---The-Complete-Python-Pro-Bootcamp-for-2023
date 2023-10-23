import React, { useState, useEffect } from 'react';
import "./styles/NavbarStyles.css";
import { NavLink, /*useLocation*/ } from 'react-router-dom';
import LogoImage from "../components/assets/logopng.png"
import { CgMenuRight, CgClose } from "react-icons/cg";
import { MdPhone } from "react-icons/md";
import { HiMail, HiLocationMarker } from "react-icons/hi";
import { BsFacebook, BsTwitter, BsInstagram, BsWhatsapp } from "react-icons/bs";
import { BiSearch } from "react-icons/bi"


function Navbar() {

 // const location = useLocation();

  // Map routes to their corresponding text
  
  /*const routeToText = {
    '/': 'Home',
    '/about': 'About Us',
    '/members': 'Certified Members',
    '/join': 'Join Us',
    '/resources': 'Resources',
    '/news': 'BHC-GH News',
    '/contact': 'Contact Us',
    '/donate': 'Donate',
  };

  const currentPageText = routeToText[location.pathname] || '';
  */

  const [showSecondNavbar, setShowSecondNavbar] = useState(false);
  const [click, setClick] = useState(false);
  const handleClick = () => setClick(!click);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 650 || window.innerWidth <= 992) {
        setShowSecondNavbar(true);
      } else {
        setShowSecondNavbar(false);
      }
    };

    // Call handleScroll initially to handle the case when the screen width is initially less than 992px
    handleScroll();

    window.addEventListener('scroll', handleScroll);
    window.addEventListener('resize', handleScroll);

    // Clean up the event listeners when the component unmounts
    return () => {
      window.removeEventListener('scroll', handleScroll);
      window.removeEventListener('resize', handleScroll);
    };
  }, []);

  return (
    <div className="navbar-container">
      {/* First Navbar */}
      <nav className="first-navbar">
        {/* Add your first navbar content here */}
        <div className="header-transparent">
          <NavLink to="/">
            <div className="title">
              <div className="logo-img-container">
                <img className="logo-img" src={LogoImage} alt="BHC-GHANA logo" />
              </div>
              <div className="title-text">
                BUREAU OF <br />HALAL CERTIFICATION<br />GHANA
              </div>
            </div>
          </NavLink>
          <div className="nav-menu-contact top">
            <div className='icon'>
              <div className="contact">
                House #4, Akwei Allah Rd, Madina - Accra
              </div>
              <HiLocationMarker className="icon-image" size={20}/>
            </div>
            <div className='icon'>
              <div className="contact">
                <a className="contact-link" href="tel:+233302123456" target="_blank" rel="noopener noreferrer">
                  +233 302 123 456
                </a> / 
                <a className="contact-link" href="tel:+233302123456" target="_blank" rel="noopener noreferrer">
                  +233 244 123 456
                </a> / 
                <a className="contact-link" href="tel:+233302123456" target="_blank" rel="noopener noreferrer">
                  +233 244 123 456
                </a>
              </div>
              <MdPhone className="icon-image" size={20}/>
            </div>
            <div className='icon'>
              <div className="contact">
                <a className="contact-link" href="mailto:info@bhcghana.org" target="_blank" rel="noopener noreferrer">
                  info@bhcghana.org
                </a>
              </div>
              <HiMail className="icon-image" size={20}/>
            </div>
          </div>
        </div>
        <div className="nav-menu-contact">
          <div className="nav-menu-container">
            <ul className="nav-menu">
              <NavLink to="/" className={({isActive}) => isActive ? "active-link": "non-active-class" }>
                <li>Home</li>
              </NavLink>
              <NavLink to="/about" className={({isActive}) => isActive ? "active-link": "non-active-class" }>
                <li>About</li>
              </NavLink>
              <NavLink to="/members" className={({isActive}) => isActive ? "active-link": "non-active-class" }>
                <li>Members</li>
              </NavLink>
              <NavLink to="/join" className={({isActive}) => isActive ? "active-link": "non-active-class" }>
                <li>Join Us</li>
              </NavLink>
              <NavLink to="/resources" className={({isActive}) => isActive ? "active-link": "non-active-class" }>
                <li>Resources</li>
              </NavLink>
              <NavLink to="/news" className={({isActive}) => isActive ? "active-link": "non-active-class" }>
                <li>News</li>
              </NavLink>
              <NavLink to="/contact" className={({isActive}) => isActive ? "active-link": "non-active-class" }>
                <li>Contact Us</li>
              </NavLink>
              <NavLink to="/donate" className={({isActive}) => isActive ? "active-link": "non-active-class" }>
                <li>Donate</li>
              </NavLink>
            </ul>
            <div className="icons-container icons-container-bar">
              <div className="icons">
                <div className='icon'>
                  <a href="https://www.facebook.com/bhcghana" target="_blank" rel="noopener noreferrer">
                    <BsFacebook size={20}/>
                  </a>
                </div>
                <div className='icon'>
                  <a href="https://twitter.com/bhc_ghana" target="_blank" rel="noopener noreferrer">
                    <BsTwitter size={20}/>
                  </a>
                </div>
                <div className='icon'>
                  <a href="https://www.instagram.com/bhc_ghana/" target="_blank" rel="noopener noreferrer">
                    <BsInstagram size={20}/>
                  </a>
                </div>
                <div className='icon'>
                  <a href="https://wa.me/+233276277041" target="_blank" rel="noopener noreferrer">
                    <BsWhatsapp size={20}/>
                  </a>
                </div>
              </div>
            </div>
          </div>
          <div className="page">
            {/*{currentPageText}*/}
            <div className="search-container">
              <div className="search-icon-btn">
                <BiSearch size={25}/>
              </div>
              <div className="search-input">
                <input type="search" className="search-bar" placeholder="Search..." />
              </div>
            </div>
          </div>
        </div>
      </nav>

      {/* Second Navbar (conditionally visible) */}
      {showSecondNavbar && (
        <nav className="second-navbar">
          {/* Add your second navbar content here */}
          <div className="header">
            <NavLink to="/">
              <div className="title">
                <div className="logo-img-container">
                  <img className="logo-img" src={LogoImage} alt="BHC-GHANA logo" />
                </div>
                <div className="title-text">BUREAU OF<br />HALAL CERTIFICATION<br />GHANA</div>
              </div>
            </NavLink>
            <ul className={click ? "nav-menu active" : "nav-menu"}>
              <div className="nav-menu-search-container hide-container">
                <div className="search-icon-btn">
                  <BiSearch size={30}/>
                </div>
                <div className="search-input">
                  <input type="search" className="search-bar" placeholder="Search..." />
                </div>
              </div>
              <NavLink to="/"><li>Home</li></NavLink>
              <NavLink to="/about"><li>About</li></NavLink>
              <NavLink to="/members"><li>Members</li></NavLink>
              <NavLink to="/join"><li>Join Us</li></NavLink>
              <NavLink to="/resources"><li>Resources</li></NavLink>
              <NavLink to="/news"><li>News</li></NavLink>
              <NavLink to="/contact" className="contact"><li>Contact Us</li></NavLink>
              <NavLink to="/donate"><li className="donate">Donate</li></NavLink>
              <div className="icons nav-menu-icons-container hide-container">
                <div className="follow-us-container">
                  <div className="nav-menu-icons">
                    <div className='icon'>
                      <a href="https://www.facebook.com/bhcghana" target="_blank" rel="noopener noreferrer">
                        <BsFacebook size={30} />
                      </a>
                    </div>
                    <div className='icon'>
                      <a href="https://twitter.com/bhc_ghana" target="_blank" rel="noopener noreferrer">
                        <BsTwitter size={30}/>
                      </a>
                    </div>
                    <div className='icon'>
                      <a href="https://www.instagram.com/bhc_ghana/" target="_blank" rel="noopener noreferrer">
                        <BsInstagram size={30}/>
                      </a>
                    </div>
                    <div className='icon'>
                      <a href="https://wa.me/+233276277041" target="_blank" rel="noopener noreferrer">
                        <BsWhatsapp size={30}/>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </ul>
            <div className="hamburger" onClick = {handleClick}>
                {click ? (<CgClose size={30} style={{ color: "#1f3f32", transition: "1s"}}/>) : (<CgMenuRight size={30} style={{ color: "#1f3f32" , transition: "1s"}}/>)}  
            </div>
          </div>
        </nav>
      )}
    </div>
  );
}

export default Navbar
