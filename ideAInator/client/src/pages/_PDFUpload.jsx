import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './uploadpdf.css';

function UploadPDF() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [uploadStatus, setUploadStatus] = useState("");
    const [isLoading, setIsLoading] = useState(false); // State for loading animation
    const [uploadSuccess, setUploadSuccess] = useState(false); // State to track successful upload

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleUpload = async (event) => {
        event.preventDefault();
        if (!selectedFile) {
            setUploadStatus("Please select a PDF file to upload.");
            return;
        }

        const formData = new FormData();
        formData.append("file", selectedFile);

        setIsLoading(true); // Start loading animation
        setUploadStatus("");
        setUploadSuccess(false); // Reset success state

        try {
            const response = await fetch('http://127.0.0.1:8000/upload/', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                setUploadStatus("File uploaded successfully!");
                setUploadSuccess(true); // Mark upload as successful
                setSelectedFile(null); // Reset file selection
            } else {
                setUploadStatus("Failed to upload file.");
            }
        } catch (error) {
            setUploadStatus("An error occurred during upload.");
            console.error("Upload error:", error);
        } finally {
            setIsLoading(false); // Stop loading animation
        }
    };

    return (
        <div className="upload-container">
            <h2>Upload a PDF</h2>
            <form onSubmit={handleUpload}>
                <input
                    type="file"
                    accept="application/pdf"
                    onChange={handleFileChange}
                />
                <button type="submit" disabled={isLoading}>
                    {isLoading ? "Uploading..." : "Upload"}
                </button>
            </form>
            {selectedFile && <p>Selected file: {selectedFile.name}</p>}
            {uploadStatus && <p className="upload-status">{uploadStatus}</p>}

            {/* Show "Start Chatting" button if upload is successful */}
            {uploadSuccess && (
                <div className="success-actions">
                    <Link to="/chat" className="chat-button">
                        Start Chatting
                    </Link>
                </div>
            )}

            {/* Loading animation */}
            {isLoading && (
                <div className="loading-spinner">
                    <div className="spinner"></div>
                </div>
            )}
        </div>
    );
}

export default UploadPDF;
