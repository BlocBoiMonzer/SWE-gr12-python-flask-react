import './HomePage.css'; // Import the CSS file
import Button from './Button'; // Import the Button component

const HomePage = () => {
  return (
    <div className="container">
      <img className="header-image" src="https://image.jimcdn.com/app/cms/image/transf/none/path/sa6549607c78f5c11/image/ia75200d7d26d4766/version/1463569446/nice-france.jpg" alt="Lokale reiser bilde" />
      <h1>Lokale Reise App</h1>
      <p>Utforsk spennende reisemål i ditt nærområde!</p>
      <Button href="/login">Logg inn</Button>
      <Button href="/register">Registrer</Button>
    </div>
  );
};

export default HomePage;