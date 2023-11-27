// import { useState, useEffect } from 'react'
import { BrowserRouter as BrowserRouter, Route, Routes } from 'react-router-dom';
import Navbar from './Navbar';
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import TourList from './TourList';
import UserRegistration from './UserRegistration';
import HomePage from './HomePage';
import UserLogin from './UserLogin';
import UserProfile from './UserProfile';
import Logout from './Logout';


// Placeholder components
// const Home = () => <h1>Home Page</h1>;
// const Register = () => <h1>Register Page</h1>;
// const Login = () => <h1>Login Page</h1>;
// const User = () => <h1>User Page</h1>;

function App() {
  // my code to test the api
  
  // const [data, setData] = useState([{}])

  // useEffect(() =>{
  //   fetch("http://127.0.0.1:5000/members").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       setData(data)
  //       console.log(data)
  //     }
  //   )
  // }, [])


  return (
    <>
    <BrowserRouter>
      <Navbar/>
      <Routes>
      
          <Route path='/' element={<HomePage />} />
          <Route path='/register' element={<UserRegistration />} />
          <Route path='/login' element={<UserLogin />} />
          <Route path='/user' element={<UserProfile />} />
          <Route path='/tours' element={<TourList />} />
          <Route path='/logout' element={<Logout />} />


      </Routes>
    </BrowserRouter>

    </>
  )
}

export default App


      {/* <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>


      </div>
      <h1 className="logo" >Monzer + Vite + React</h1>


      <div>

        {(typeof data.members === 'undefined') ? (
          <p>Loading...</p>
        ): (
          data.members.map((member, i) => (
            <p key={i}> {member} </p>
          )))}
      </div>

      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p> */}