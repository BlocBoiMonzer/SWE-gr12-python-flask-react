import React, { FormEvent, useState } from 'react';

interface User {
  username: string;
  password: string;
  email: string;
}

const UserRegistration: React.FC = () => {
  const [user, setUser] = useState<User>({ username: '', password: '', email: '' });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUser({
      ...user,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    // Send user data to server
    try {
      const response = await fetch('http://localhost:3000/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
      });
      const data = await response.json();
      // insert Handle response
    } catch (error) {
      // insert Handle error
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="username" value={user.username} onChange={handleChange} placeholder="Username" required />
      <input type="password" name="password" value={user.password} onChange={handleChange} placeholder="Password" required />
      <input type="email" name="email" value={user.email} onChange={handleChange} placeholder="Email" required />
      <button type="submit">Register</button>
    </form>
  );
};

export default UserRegistration;