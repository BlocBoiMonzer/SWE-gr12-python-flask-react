import { useEffect, useState } from 'react';

// typescript activities lol
interface Tour {
  id: number;
  name: string;
  description: string;
}

function TourList() {
  const [tours, setTours] = useState<Tour[]>([]); // Use the Tour type here

  useEffect(() => {
    fetch('http://localhost:3000/tours')
      .then(response => response.json())
      .then(data => setTours(data));
  }, []);

  return (
    <div>
      {tours.map(tour => (
        <div key={tour.id}>
          <h2>{tour.name}</h2>
          <p>{tour.description}</p>
          <p>hello world</p>
        </div>
      ))}
    </div>
  );
}

export default TourList;