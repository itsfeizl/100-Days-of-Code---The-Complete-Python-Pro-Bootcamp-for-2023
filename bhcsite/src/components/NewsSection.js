// News.js
import React from 'react';
import './styles/NewsSectionStyles.css';
import { Link, NavLink } from 'react-router-dom';
import image1 from './assets/placeholder-img.jpg';

const NewsSection = () => {
  return (
    <div className="section-container">
      <div className="news-header">
        <h2 className="section-title">News & Events</h2>
        <div className="more-news">
          <Link to="/news" className="more-link">
            More News & Events
          </Link>
        </div>
      </div>
      <div className="news-cards">
        <div className="news-card">
          <div className="news-card-inner">
            <img className="news-img" src={image1} alt="placeholder" />
            <div className="date-label">
              <div className="date">Oct 01</div>
              <div className="label">News</div>
            </div>
          </div>
          <div className="news-text">
            <h3 className="news-headline">Don't Compromise on Halal - Sheikh Abdullatif</h3>
            <p className="news-description">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod...<span><em>more</em></span>
            </p>
          </div>
        </div>
        <div className="news-card">
          <div className="news-card-inner">
            <img className="news-img" src={image1} alt="placeholder" />
            <div className="date-label">
              <div className="date">Oct 20</div>
              <div className="label">News</div>
            </div>
          </div>
          <div className="news-text">
            <h3 className="news-headline">BHC Ghana to Host Halal and Tourism Promotion Conference</h3>
            <p className="news-description">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod...<span><em>more</em></span>
            </p>
          </div>
        </div>
        <div className="events-card">
          <h3 className="events-title">Upcoming Events</h3>
          <div className="event">
            <div className="event-date">
              <div className="event-date-day">30</div>
              <div className="event-date-month">SEP</div>
            </div>
            <h4>Halal Insights Webinar Series with Sheikh Abdullatif A. Sheikh</h4>
          </div>
          <div className="event">
            <div className="event-date">
              <div className="event-date-day">28</div>
              <div className="event-date-month">OCT</div>
            </div>
            <h4>Hayes Awareness Programme – The Importance of Halal Food</h4>
          </div>
          <div className="event">
            <div className="event-date">
              <div className="event-date-day">01</div>
              <div className="event-date-month">NOV</div>
            </div>
            <h4>Hayes Awareness Programme – The Importance of Halal Food</h4>
          </div>
          <div className="event">
            <div className="event-date">
              <div className="event-date-day">05</div>
              <div className="event-date-month">DEC</div>
            </div>
            <h4>Ghana Halal and Tourism Promotion Conference</h4>
          </div>
        </div>
      </div>
      <div className="more-news more-news-small">
        <NavLink to="/news" className="more-link">
          More News & Events
        </NavLink>
      </div>
    </div>
  );
};

export default NewsSection;
