import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const Logout: React.FC = () => {
  const navigate = useNavigate();

  useEffect(() => {
    sessionStorage.clear(); // Clear the session storage
    navigate('/'); // Redirect to home page
  }, [navigate]);

  return null; // This component doesn't render anything cuz i it deosn't need it
};

export default Logout;