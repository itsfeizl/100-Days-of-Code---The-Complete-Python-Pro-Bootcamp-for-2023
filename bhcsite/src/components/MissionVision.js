import React, { useState } from 'react';
import "./styles/MissionVisionStyles.css"

const MissionVision = () => {
    const [showMission, setShowMission] = useState(true);

    const mission = "Our mission is to provide comprehensive Halal auditing, certification, training, and consulting services that empower businesses to meet the highest standards of Halal compliance. We monitor, inspect and certify Halal products and outlets for the benefit of the Muslim community. We aim to educate and guide organizations to understand and implement Halal practices, publish and update record of companies who comply, thereby contributing to the well-being of diverse communities and promoting ethical and responsible business conduct.";

    const vision = "Our vision for the future is to be the most transparent, trustworthy and reliable Halal monitoring, inspection and Certification Company ensuring Halal integrity across industries, fostering trust and transparency in the market, and enhancing the quality of products and services for the benefit of consumers and businesses.";

    const toggleMission = () => {
        setShowMission(true);
    };
    
    const toggleVision = () => {
        setShowMission(false);
    };


    return (
        <div className="mission-vision-section-container">
            <div className="mission-vision-btns-container">
                <div className="mission-vision-btns">
                <div
                    className={`mission-vision ${showMission ? 'active' : ''}`}
                    onClick={toggleMission}
                >
                    Mission
                </div>
                <div
                    className={`mission-vision ${!showMission ? 'active' : ''}`}
                    onClick={toggleVision}
                >
                    Vision
                </div>
                </div>
            </div>

            <div className="mission-vision-text">
                
                <p>{showMission ? mission : vision}</p>
            </div>
        </div>
    )
}

export default MissionVision;