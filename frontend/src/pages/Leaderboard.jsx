import React from 'react';
import RankingTable from '../components/RankingTable';
import ProgressCharts from '../components/ProgressCharts';
import BadgeDisplay from '../components/BadgeDisplay';

/**
 * Leaderboard page component that displays user rankings and progress.
 */
const Leaderboard = () => {
    return (
        <div className="leaderboard">
            <RankingTable />
            <ProgressCharts />
            <BadgeDisplay />
        </div>
    );
};

export default Leaderboard;
