import React from 'react';
import HeroSection from '../components/HeroSection';
import FeaturedPortfolios from '../components/FeaturedPortfolios';
import CommunityHighlights from '../components/CommunityHighlights';
import MentorShowcase from '../components/MentorShowcase';
import CallToAction from '../components/CallToAction';

/**
 * Home page component that serves as the landing page for the application.
 */
const Home = () => {
    return (
        <div className="home">
            <HeroSection 
                image="https://example.com/hero-image.jpg" 
                title="Welcome to Our Platform" 
                description="Join us to explore amazing portfolios and connect with mentors!"
            />
            <FeaturedPortfolios />
            <CommunityHighlights />
            <MentorShowcase />
            <CallToAction />
        </div>
    );
};

export default Home;
