import React from 'react';
import './SingleTour.css'; // Import the CSS file

interface SingleTourProps {
  tour: {
    id: number;
    name: string;
    description: string;
  };
}

const SingleTour: React.FC<SingleTourProps> = ({ tour }) => {
  return (
    <div className="tour-card">
      <h2>{tour.name}</h2>
      <p>{tour.description}</p>
    </div>
  );
};

export default SingleTour;