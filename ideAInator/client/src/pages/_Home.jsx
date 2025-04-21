import React, { useEffect, useState } from "react";
import "./home.css";
import { Link } from "react-router-dom";

function Home() {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedSemester, setSelectedSemester] = useState("fall2024");
  const [selectedCourse, setSelectedCourse] = useState("");

  // Fetch profile data
  const fetchProfile = async () => {
    setLoading(true);
    try {
      const response = await fetch("/profile/");
      if (!response.ok) throw new Error("Failed to fetch profile");
      const data = await response.json();
      setProfile(data);
      setLoading(false);
    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProfile();
  }, []);

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="container">
      <div className="banner">
        <h1 className="welcomeText">
          Welcome, {profile.display_name.charAt(0).toUpperCase() + profile.display_name.slice(1)}
        </h1>
      </div>
      <div className="content">
        <p className="blurb">
          This site analyzes semesterly surveys from students and serves as a useful chatbot
          to help improve your teaching style.
        </p>

        <div className="selectorContainer">
          <label className="label">
            Select Course:
            <select
              className="select"
              value={selectedCourse}
              onChange={(e) => setSelectedCourse(e.target.value)}
            >
              {profile.classes && profile.classes.length > 0 ? (
                profile.classes.map((course, index) => (
                  <option key={index} value={course}>
                    {course}
                  </option>
                ))
              ) : (
                <option value="">No courses available</option>
              )}
            </select>
          </label>
        </div>

        <div className="buttonContainer">
          <Link
            to="/chat"
            className="mainButton"
            state={{ semester: selectedSemester, course: selectedCourse }}
          >
            Start Conversation with AI
          </Link>
          <Link
            to="/uploadpdf"
            className="mainButton"
          >
            Upload PDF
          </Link>
        </div>
      </div>
    </div>
  );
}

export default Home;
