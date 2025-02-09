import React from 'react';
import CommunityList from '../components/CommunityList';
import TrendingPosts from '../components/TrendingPosts';
import DiscussionThreads from '../components/DiscussionThreads';

/**
 * Community page component that displays community-related content.
 */
const Community = () => {
    return (
        <div className="community">
            <CommunityList />
            <TrendingPosts />
            <DiscussionThreads />
        </div>
    );
};

export default Community;
