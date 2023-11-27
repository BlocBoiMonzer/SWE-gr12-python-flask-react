import React, { useEffect, useState } from 'react';
import './UserProfile.css';
import Footer from './Footer';

interface User {
  username: string;
  image_filename: string;
}

const UserProfile = () => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const storedUser = sessionStorage.getItem('user');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }
  }, []);

  const handleImageUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    // Handle the image upload here
    console.log(event.target.files);
  };

  
  if (!user) {
    return <p>Loading...</p>;
  }

  console.log(user.username + " lolll")
  // FIX THIS USERNAME DISPLAYING ISSUE
  return (
    <div>
      <header>
        <h1>Welcome, {user.username}!</h1>
      </header>

      <main>
        <section>
          <h2>Profile Picture</h2>
          {user.image_filename ? (
            <div>
              <img src={`/uploads/${user.image_filename}`} alt="Profile" />
              <p>{user.image_filename}</p>
            </div>
          ) : (
            <p>No profile picture uploaded.</p>
          )}
          <form>
            <input type="file" onChange={handleImageUpload} />
            <button type="submit">Upload New Picture</button>
          </form>
        </section>
      </main>

      <Footer></Footer>
    </div>
  );
};

export default UserProfile;
