import React, { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import './chat.css';

function Chat() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const [isThinking, setIsThinking] = useState(false); // Track if the AI is thinking
    const [isSaved, setIsSaved] = useState(false); // Track if the chat has been saved
    const chatEndRef = useRef(null); // Reference to the bottom of the chat

    // Scroll to the bottom of the chat
    const scrollToBottom = () => {
        if (chatEndRef.current) {
            chatEndRef.current.scrollIntoView({ behavior: 'smooth' });
        }
    };

    useEffect(() => {
        scrollToBottom(); // Scroll when messages are updated
    }, [messages]);

    const sendMessageToBackend = async (text) => {
        try {
            const response = await fetch('http://127.0.0.1:8000/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json(); // Assuming the response has JSON with the AI's message
            return data.response; // Adjust `data.response` to match your backend's response structure
        } catch (error) {
            console.error("Error sending message to backend:", error);
            throw error; // Rethrow the error for the caller to handle
        }
    };

    const handleSendMessage = async (text) => {
        const userMessage = { user: "You", text };
        setMessages((prevMessages) => [...prevMessages, userMessage]);
        setInput("");
        setIsThinking(true); // Start the thinking animation

        try {
            // Call the backend logic function
            const aiResponseText = await sendMessageToBackend(text);

            // Update the chat with the AI's response
            const aiResponse = { user: "AI", text: aiResponseText };
            setMessages((prevMessages) => [...prevMessages, aiResponse]);
        } catch (error) {
            // Handle errors (e.g., show an error message in the UI)
            const errorMessage = { user: "System", text: "Failed to get a response from the AI." };
            setMessages((prevMessages) => [...prevMessages, errorMessage]);
        } finally {
            setIsThinking(false); // Stop the thinking animation
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (input.trim()) {
            handleSendMessage(input);
        }
    };

    const handlePromptClick = (prompt) => {
        handleSendMessage(prompt);
    };

    // Function to save the chat conversation to the user's profile
    const handleSaveChat = async () => {
        try {
            const response = await fetch('/save_conversation/', { // Use the correct backend endpoint
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ conversation: messages }), // Send the conversation history
            });
    
            if (response.ok) {
                setIsSaved(true); // Mark the conversation as saved
            } else {
                const errorData = await response.json();
                console.error("Failed to save conversation:", errorData.error || "Unknown error");
            }
        } catch (error) {
            console.error("Error saving conversation:", error);
        }
    };
    
    return (
        <div className="chat-container">
            <div className="chat-header">
                <h2>Chat with AI</h2>
            </div>
            <div className="chat-body">
                <div className="chat-prompts">
                    <h4>Premade Prompts:</h4>
                    <ul>
                        <li onClick={() => handlePromptClick("What are three things I did well?")}>What are three things I did well?</li>
                        <li onClick={() => handlePromptClick("What are three things students disliked?")}>What are three things students disliked?</li>
                        <li onClick={() => handlePromptClick("How can I improve?")}>How can I improve?</li>
                        <li onClick={() => handlePromptClick("Give me three quotes that summarize the main atmosphere of the class.")}>Give me three quotes that summarize the main atmosphere of the class.</li>
                    </ul>
                </div>
                <div className="chat-display">
                    {messages.map((message, index) => (
                        <div key={index} className="message">
                            <strong>{message.user}: </strong>
                            {message.user === "AI" ? (
                                <ReactMarkdown>{message.text}</ReactMarkdown> // Render AI's response as Markdown
                            ) : (
                                <span>{message.text}</span>
                            )}
                        </div>
                    ))}
                    {/* Thinking animation */}
                    {isThinking && (
                        <div className="thinking">
                            <strong>Reviewing Survey Data</strong> <span className="thinking-dots"></span>
                        </div>
                    )}
                    {/* Empty div to scroll to */}
                    <div ref={chatEndRef}></div>
                </div>
            </div>
            <form className="chat-input" onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Type your message here..."
                />
                <button type="submit">Send</button>
            </form>
            <button onClick={handleSaveChat} disabled={isSaved} className="save-button">
                {isSaved ? "Chat Saved" : "Save Chat"}
            </button>
        </div>
    );
}

export default Chat;
