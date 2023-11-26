import './Footer.css'

const Footer: React.FC = () => {
    return (
      <footer>
        <p>&copy; 2023 Gruppe 12. All rights reserved.</p>
        <nav>
          <a href="/">Home</a> |
          <a href="/profile">Profile</a> |
          <a href="/logout">Logout</a>
        </nav>
      </footer>
    );
  };
  
  export default Footer;