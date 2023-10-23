// ServicesSection.js
import React from 'react';
import './styles/ServicesSectionStyles.css';

const ServicesSection = () => {
  // Define your services data here.
  const services = [
    {
      title: 'Halal Auditing',
      description: 'Our rigorous auditing process ensures businesses comply with Halal standards, providing consumers with the assurance that products and services are genuinely Halal.',
    },
    {
      title: 'Certification',
      description: 'We offer trusted Halal certification, granting businesses the credibility they need to demonstrate their commitment to Halal integrity.',
    },
    {
      title: 'Education',
      description: 'Our training programs equip businesses with the knowledge and skills to implement and maintain Halal practices throughout their operations.',
    },
    {
      title: 'Consultation',
      description: 'We provide expert consulting services to guide businesses in navigating the complexities of Halal compliance, tailored to their specific needs and industry requirements.',
    },
    // Add more services as needed
  ];

  return (
    <div className="section-container services-section">
      <div className="services-header">
        <h2 className="section-title">Our Services</h2>
      </div>
      
      <div className="services-list">
        {services.map((service, index) => (
          <div key={index} className="service-card">
            <h3 className="service-title">{service.title}</h3>
            <p className="service-description">{service.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ServicesSection;
