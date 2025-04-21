import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "./transcript.css";

function Transcript() {
  const { id } = useParams(); // Get the conversation ID from the URL
  const [conversation, setConversation] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch the conversation
  useEffect(() => {
    const fetchConversation = async () => {
      try {
        const response = await fetch(`/transcript/${id}/`);
        if (!response.ok) throw new Error("Failed to fetch transcript");
        const data = await response.json();
        setConversation(data.conversation); // Set the fetched conversation
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchConversation();
  }, [id]);

  // Function to generate a downloadable text file
  const downloadTranscript = () => {
    if (!conversation) return;

    const transcriptContent = conversation
      .map((msg) => `${msg.user}: ${msg.text}`)
      .join("\n\n"); // Format transcript with newlines

    const blob = new Blob([transcriptContent], { type: "text/plain" }); // Create a Blob object
    const url = URL.createObjectURL(blob); // Create a URL for the Blob
    const link = document.createElement("a"); // Create an anchor element
    link.href = url;
    link.download = `transcript_${id}.txt`; // Set the filename
    document.body.appendChild(link); // Append the link to the DOM
    link.click(); // Programmatically click the link to trigger download
    document.body.removeChild(link); // Clean up by removing the link
  };

  if (loading) {
    return <div className="loading">Loading transcript...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="transcript">
      {/* Download Button */}
      <div className="transcript-header">
        <button onClick={downloadTranscript} className="download-btn">
          Download Transcript
        </button>
      </div>
      <h2>Conversation Transcript</h2>
      <ul>
        {conversation && conversation.length > 0 ? (
          conversation.map((msg, index) => (
            <li key={index} className={`message ${msg.user === "AI" ? "ai" : "user"}`}>
              <strong>{msg.user}:</strong>
              <p>{msg.text}</p>
            </li>
          ))
        ) : (
          <p>No messages in this conversation.</p>
        )}
      </ul>
    </div>
  );
}

export default Transcript;
