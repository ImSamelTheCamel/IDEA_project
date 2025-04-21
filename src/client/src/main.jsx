import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import Home from './pages/_Home.jsx';
import Chat from './pages/_Chat.jsx';
import Profile from './pages/_Profile.jsx';
import UploadPDF from './pages/_PDFUpload.jsx';
import Transcript from './pages/_Transcript.jsx'; // Import the Transcript component
import './index.css';
import 'vite/modulepreload-polyfill';
import { createHashRouter, RouterProvider } from 'react-router-dom';

const router = createHashRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/chat",
        element: <Chat />,
      },
      {
        path: "/profile",
        element: <Profile />,
      },
      {
        path: "/uploadpdf",
        element: <UploadPDF />,
      },
      {
        path: "/transcript/:id", // Correct the syntax for a route with parameters
        element: <Transcript />,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router} />
);
