import React, { FormEvent, useState } from 'react';
import './UserRegistration.css'; 
import Button from './Button.tsx';

interface User {
  firstname: string;
  lastname: string;
  phonenumber: string;
  address: string;
  email: string;
  username: string;
  password: string;
}

const UserRegistration: React.FC = () => {
  const [user, setUser] = useState<User>({ firstname: '', lastname: '', phonenumber: '', address: '', email: '', username: '', password: '' });
  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUser({
      ...user,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    // Sends user data to server
    try {
      const response = await fetch('http://localhost:3000/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
      });
      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.error);
      }
      // insert Handle response
    } catch (error: any) {
      // insert Handle error
      setError(error.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        First Name:
        <input type="text" name="firstname" value={user.firstname} onChange={handleChange} required />
      </label>
      <label>
        Last Name:
        <input type="text" name="lastname" value={user.lastname} onChange={handleChange} required />
      </label>
      <label>
        Phone Number:
        <input type="text" name="phonenumber" value={user.phonenumber} onChange={handleChange} required />
      </label>
      <label>
        Address:
        <input type="text" name="address" value={user.address} onChange={handleChange} required />
      </label>
      <label>
        Email:
        <input type="email" name="email" value={user.email} onChange={handleChange} required />
      </label>
      <label>
        Username:
        <input type="text" name="username" value={user.username} onChange={handleChange} required />
      </label>
      <label>
        Password:
        <input type="password" name="password" value={user.password} onChange={handleChange} required />
      </label>
      <Button onClick={(e) => { e.preventDefault(); handleSubmit(e); }}>Register</Button>
      
      {error && <p>{error}</p>}
    </form>
  );
};

export default UserRegistration;