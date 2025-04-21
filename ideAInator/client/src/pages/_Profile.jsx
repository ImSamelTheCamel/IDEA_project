import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom"; // Import Link for client-side navigation
import "./profile.css";

function Profile() {
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [editMode, setEditMode] = useState(false);
  const [formData, setFormData] = useState({
    classes: "",
    conversations: [],
  });

  // Fetch profile data
  const fetchProfile = async () => {
    setLoading(true);
    try {
      const response = await fetch("/profile/");
      if (!response.ok) throw new Error("Failed to fetch profile");
      const data = await response.json();
      setProfile(data);
      setFormData({
        classes: data.classes.join(", "),
      });
      setLoading(false);
    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  };

  // Save updated profile data
  const saveProfile = async (e) => {
    e.preventDefault();
    try {
      const updatedData = {
        classes: formData.classes.split(",").map((cls) => cls.trim()),
        conversations: formData.conversations,
      };

      const response = await fetch("/profile/", {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updatedData),
      });

      if (!response.ok) throw new Error("Failed to update profile");

      setEditMode(false);
      fetchProfile();
    } catch (err) {
      setError(err.message);
    }
  };

  useEffect(() => {
    fetchProfile();
  }, []);

  if (loading) {
    return <div className="loading">Loading profile...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="profile-container">
      <div className="profile-card">
        <h1>
          {profile.display_name
            ? profile.display_name.charAt(0).toUpperCase() + profile.display_name.slice(1)
            : "Guest"}
          's Profile
        </h1>


        {/* Classes Section */}
        <div className="profile-section">
          <h3>Classes</h3>
          {editMode ? (
            <input
              type="text"
              value={formData.classes}
              onChange={(e) =>
                setFormData({ ...formData, classes: e.target.value })
              }
              placeholder="Enter classes separated by commas"
            />
          ) : (
            <ul>
              {profile.classes && profile.classes.length > 0 ? (
                profile.classes.map((cls, index) => <li key={index}>{cls}</li>)
              ) : (
                <p>No classes available.</p>
              )}
            </ul>
          )}
        </div>

        {/* Conversations Section */}
        <div className="profile-section">
          <h3>Conversations</h3>
          {editMode ? (
            <div />
          ) : (
            <ul>
              {profile.conversations && profile.conversations.length > 0 ? (
                profile.conversations.map((conversation, index) => (
                  <li key={index}>
                    <Link to={`/transcript/${index}`} className="conversation-link">
                      Conversation {index + 1}
                    </Link>
                  </li>
                ))
              ) : (
                <p>No conversations available. Start a new chat to create one!</p>
              )}
            </ul>
          )}
        </div>

        {/* Actions */}
        <div className="profile-actions">
          {editMode ? (
            <>
              <button onClick={saveProfile} className="save-btn">
                Save
              </button>
              <button onClick={() => setEditMode(false)} className="cancel-btn">
                Cancel
              </button>
            </>
          ) : (
            <button onClick={() => setEditMode(true)} className="edit-btn">
              Edit Profile
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

export default Profile;
