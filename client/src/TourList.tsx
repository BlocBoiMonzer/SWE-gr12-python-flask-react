import { useEffect, useState } from 'react';
import Footer from './Footer';
import SingleTour from './SingleTour'; // Import the SingleTour component

// Typescript being typescript lol
interface Tour {
  id: number;
  name: string;
  description: string;
}

function TourList() {
  const [tours, setTours] = useState<Tour[]>([]); // Use the Tour type here

  useEffect(() => {
    fetch('http://localhost:3000/tours', { credentials: 'include' }) // Include credentials
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => setTours(data))
      .catch(error => console.log('Fetch error: ', error));
  }, []);

  return (
    <div>
      {tours.map(tour => (
        <SingleTour key={tour.id} tour={tour} /> 
      ))}
      <Footer></Footer>
    </div>
  );
}

export default TourList;