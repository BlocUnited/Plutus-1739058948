import React from 'react';
import ProfileHeader from '../components/ProfileHeader';
import PortfolioGrid from '../components/PortfolioGrid';
import AchievementsSection from '../components/AchievementsSection';
import SocialLinks from '../components/SocialLinks';

/**
 * Profile page component that displays user profile information.
 */
const Profile = () => {
    return (
        <div className="profile">
            <ProfileHeader />
            <PortfolioGrid />
            <AchievementsSection />
            <SocialLinks />
        </div>
    );
};

export default Profile;
