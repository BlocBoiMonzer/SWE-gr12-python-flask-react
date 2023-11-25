// import { useState, useEffect } from 'react'
import { BrowserRouter as BrowserRouter, Route, Routes } from 'react-router-dom';
import Navbar from './Navbar';
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import TourList from './TourList';

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

        <Route path='/'>

        </Route>

        <Route path='register'>

        </Route>
        
        <Route path='/login'>
          
        </Route>

        <Route path='/user'>
          
        </Route>

        <Route path='/tours'>
          <TourList />
        </Route>
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