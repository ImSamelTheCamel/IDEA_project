import React from 'react';
import { Outlet, Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="navbar">
      <ul>
        <li>
        <Link to="/#">
              <span className="tooltip">Home</span>
        </Link>
        </li>
        <li>
        <Link to="/chat">
              <span className="tooltip">Chat</span>
        </Link>
        </li>
        <li>
        <Link to="/profile">
              <span className="tooltip">Profile</span>
        </Link>
        </li>
        <li><a href="#">Resources</a></li>
        <li><a href="#">About AI</a></li>
      </ul>
    </nav>
  );
}

export default Navbar;
