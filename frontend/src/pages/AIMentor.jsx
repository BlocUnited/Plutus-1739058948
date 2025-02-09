import React from 'react';
import ChatInterface from '../components/ChatInterface';
import SuggestedPrompts from '../components/SuggestedPrompts';
import FeedbackDisplay from '../components/FeedbackDisplay';

/**
 * AIMentor page component that provides AI mentoring features.
 */
const AIMentor = () => {
    return (
        <div className="ai-mentor">
            <ChatInterface messages={[]} inputPlaceholder="Type your message..." />
            <SuggestedPrompts />
            <FeedbackDisplay />
        </div>
    );
};

export default AIMentor;
