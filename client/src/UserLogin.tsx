import React, { useState } from 'react';
import './UserLogin.css'; // Import the CSS file
import Button from './Button';

const UserLogin: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = () => {
    // Perform login logic here, e.g. make a POST request to the server with username and password
    fetch('http://localhost:3000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Innlogging feilet lol');
        }
        return response.json();
      })
      .then((data) => {
        // Handle successful login, e.g. store user data in session
        sessionStorage.setItem('user', JSON.stringify(data));
        // Redirect to the user page or perform other actions
      })
      .catch((error) => {
        setError(`Innlogging feilet. Feil brukernavn eller passord. Error: ${error.message}`);
      });
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <Button onClick={handleLogin}>Login</Button>
      {error && <p className="error-message">{error}</p>}
    </div>
  );
};

export default UserLogin;