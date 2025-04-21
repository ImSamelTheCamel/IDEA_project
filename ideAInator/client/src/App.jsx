import { useState } from 'react'
import {Outlet, Link} from 'react-router-dom'
import logo from './assets/profile.png'

function App() {
  const [count, setCount] = useState(0)

  async function logout() {
    const res = await fetch("/registration/logout/", {
      credentials: "same-origin", // include cookies!
    });

    if (res.ok) {
      // navigate away from the single page app!
      window.location = "/registration/sign_in/";
    } else {
      // handle logout failed!
    }
  }

  return (
    <>
    <nav className="navbar">
          <a href="/#">Home</a>
          <a href="#/chat">Chat</a>
          <a href="#/profile">Profile</a>
          <a href="#/uploadpdf">Upload PDF's</a>
          <a className="icon" onClick={logout}>
            <span className="tooltip">Logout</span>
          </a>
    </nav>
  
      <header>
        <div className='logo-container'>
        <Link to="/">
            <img src={logo} className="logo" width="616" alt="Utah State"></img>
          </Link>
      </div>
      <div>
        Utah State University IDEA Surveys
        </div>
      </header>
      
        <Outlet />
      
    </>
  );
}



export default App;