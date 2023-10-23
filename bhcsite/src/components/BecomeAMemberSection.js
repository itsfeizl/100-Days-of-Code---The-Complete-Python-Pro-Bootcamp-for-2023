import React from 'react';
import "./styles/BecomeAMemberSectionStyles.css"
import { Link } from 'react-router-dom';
import pack from "./assets/preapppack.jpg"


const BecomeAMemberSection = () => {
  
  return (
    <div className="section-container get-certified" >
        <div className="get-certified-text">
            <p>Unlock a wider market and demonstrate your commitment to inclusivity</p>
            <h2>GET CERTIFIED TODAY!</h2>
            <div className="apply-checkstat-btns">
                <Link to="/join" style={{display: "flex"}} className="apply-support-link">
                    <div className="start-application-link">
                        Start Application
                    </div>
                </Link>
                <Link to="/join" style={{display: "flex"}} className="apply-support-link">
                    <div className="start-application-link support-us">
                        Check Certification
                    </div>
                </Link>
            </div>
        </div>  
        <div className="learn-more">
            <div className="pack-container">
                <img className="pack-img" src={pack} alt="Pre application pack" />
            </div>
            <p className="pack-download"><Link to="" className="more-link">Download</Link> to learn more.</p>
        </div>
    </div>
  );
};

export default BecomeAMemberSection;