
# Introduction

## Brief Overview of IDE-AI-nator

IDE-AI-nator is an interactive Chrome plugin designed to work seamlessly with the IDEA surveys used by Utah State University to analyze the performance of instructors. The plugin will use Artificial Intelligence to help instructors learn from student surveys and find trends to improve their teaching. It will help teachers focus on relevant feedback while filtering out less useful responses.

## Purpose of Requirements Document

This document organizes and outlines the needed requirements for the "IDE-AI-nator" app. It will be used to guide the design and development process, providing a clear framework for the final product.

# Requirements

## 1. Functional Requirements

Functional requirements define the specific behaviors, features, and functions the software must perform to meet user needs.

### 1.1 ChatBox with Prompts

- **Chrome Plugin:** The chat box will function within a Chrome plugin on the Utah State University website. Users can upload PDFs for processing, and the interface will mimic the appearance of USU websites.
- **Different Prompts:** Quick access buttons will offer multiple prompt options, simplifying usage for users unfamiliar with technology or unsure of what information to request from the surveys.
- **Chat History:** Users can view and select previously asked questions to retrieve results again, useful in case of connection loss or accidental window closure.
- **PDF Processing:** The AI will scrub the uploaded PDFs to generate summaries of IDEA surveys.
- **Keyword Search:** The AI can find specific words or phrases and provide a detailed report based on those terms.
- **Language Filtering:** Offensive language will be filtered out, returning cleaned survey results.
- **Summary of Major Questions:** Focused summaries will be provided based on responses to the three major questions on IDEA surveys: general comments, suggested changes, and strengths in the class.

### 1.2 User Authentication

- **User Profiles:** Users log in with their Utah State University credentials and have access to their own survey data.
- **Microsoft Authentication:** Two-factor authentication will be used for security.
- **Credential Levels:** Certain users, such as department heads and university administrators, will have access to multiple surveys beyond their own.

### 1.3 Application Output

- **PDF Output:** Results from the AI will be downloadable as a PDF.
- **Prompts in Output:** The PDF will include the prompts given to the AI for context.
- **Quote Citation:** Specific surveys may be quoted to provide evidence of AI-generated insights.

## 2. Non-Functional Requirements

Non-functional requirements describe performance, quality, and operational constraints of the system.

### 2.1 Performance

- **Response Time:** AI analysis should be completed within 15 seconds.
- **Scalability:** The system must handle large volumes of data efficiently.
- **Storage Efficiency:** Storage and retrieval of chats and feedback must be optimized to prevent performance impact.

### 2.2 Security

- **Authentication:** Utah State University's SSO system will be used for login.
- **Access Control:** Professors and deans will only access their own survey data.
- **Privacy:** The app will comply with student data protection regulations.

### 2.3 Usability

- **Accessibility:** The app will meet WCAG 2.1 standards for accessibility.
- **User Interface:** The UI will be intuitive and easy to navigate for professors and deans.
- **Chat History:** Users will have access to past chats, which will be saved and displayed with efficient response times.
- **Download Option:** Chat histories and analysis results will be downloadable as PDF files within 5 seconds.

### 2.4 Compatibility

- **Browser Support:** The plugin will support Chrome, and prompt users to switch if they are not on Chrome.
- **PDF Generation:** Ensure all generated reports can be opened by popular PDF readers.

## 3. User Requirements

User requirements define how the system should look, feel, and behave for the end-users.

### 3.1 Sign-in and Security

- **Single Sign-On (SSO):** Secure sign-in with university credentials.
- **Encryption:** All data will be encrypted during transmission.
- **Session Timeouts:** Inactive sessions will be automatically logged out for security.

### 3.2 Access to Student Feedback

- **Feedback Organization:** Feedback will be organized by course, section, and semester with filtering options.
- **Search Functionality:** A search bar will help users find specific feedback.
- **Filtering Options:** Users can filter feedback based on sentiment, topics, or comment length.

### 3.3 AI-Generated Summaries

- **Summary Clarity:** The AI will generate clear, concise summaries of feedback.
- **Key Topic Identification:** The AI will highlight key themes, such as course content or teaching methods.
- **Context Sensitivity:** The AI will understand the context of feedback to ensure accurate summaries.

### 3.4 Quote Extraction

- **Highlight Direct Quotes:** The AI will pull relevant quotes from feedback.
- **Contextual Display:** Quotes will be presented with their surrounding context for clarity.
- **Tagging and Categorization:** Quotes will be tagged by feedback topics.

### 3.5 Improvement Suggestions Based on Feedback

- **Actionable Insights:** The AI will provide specific suggestions based on trends.
- **Feedback Weighting:** Important feedback will be prioritized.
- **Optional Suggestions:** Users can choose to request or dismiss AI suggestions.

### 3.6 Customization of AI Analysis

- **Focus Settings:** Users can customize which aspects of feedback the AI prioritizes.
- **Adjustable Sentiment Sensitivity:** Users can adjust how the AI interprets sentiment.
- **Exclusion of Irrelevant Feedback:** Irrelevant comments can be excluded from the analysis.

### 3.7 Feedback Trends Over Time

- **Historical Comparisons:** Feedback summaries from different semesters can be compared.
- **Visual Analytics:** Trends will be visualized using graphs and charts.
- **Trend Alerts:** Notifications will be provided for significant shifts in feedback trends.

### 3.8 Save and Export Summaries

- **Session Saving:** Users can save summaries for future reference.
- **Export Formats:** Summaries can be exported in PDF, CSV, or plain text formats.
- **Customization of Export:** Users can customize the content of the exported files.

### 3.9 Session History and Conversations with AI

- **Saved Conversations:** AI interactions will be automatically saved for future reference.
- **Searchable History:** Users can search session history by keywords or topics.
- **Session Organization:** Sessions will be organized by course and date for easy retrieval.

### 3.10 User-Friendly Interface

- **Intuitive Navigation:** The interface will allow for quick navigation of comments and summaries.
- **Real-Time Response:** The AI will provide real-time feedback as users adjust settings.

## 4. MoSCoW Analysis

### 4.1 Must Have

- Customer Sign-In
- Profile Types
- Qualitative Reporting
- Date Range Filter
- PDF Export
- Maintenance Alert

### 4.2 Should Have

- Filter by Course
- AI Content Warning
- AI Chatbot
- Access Control

### 4.3 Could Have

- Customizable Analysis
- Visual Reporting
- Trend Identification

### 4.4 Won't Have

- Mobile App Version
- Social Sharing

## 5. Use Case Stories

### 5.1 End-User Story

- As an end user, I want to securely sign in using Single Sign-On (SSO).
- As an end user, I want to organize student feedback by course, section, and semester.
- As an end user, I want the AI to generate concise summaries of feedback.
- As an end user, I want to exclude irrelevant or outlier comments from the analysis.

### 5.2 IDE-AI-nator Story

- As the IDE-AI-nator, I want to analyze and generate summaries of student feedback.
- As the IDE-AI-nator, I want to highlight direct quotes from student feedback.
- As the IDE-AI-nator, I want to provide actionable suggestions based on feedback trends.

### 5.3 Admin Story

- As an admin, I want to manage user roles and permissions.
- As an admin, I want to ensure data encryption and enforce session timeouts.
- As an admin, I want to monitor system performance.

### 5.4 General System Story

- As a user, I want a secure, encrypted environment.
- As a user, I want real-time feedback analysis.
- As a user, I want to compare feedback across semesters.

## 6. Use Case Diagrams

Figures representing website mapping, login page, chatbot, user data, chat history, and profile mockups.

![Diagram 1](/Images/Diagram_1.png "Diagram 1")
![Diagram 2](/Images/Diagram 2.png "Diagram 2")
![Diagram 3](/Images/Diagram 3.png "Diagram 3")
![Diagram 4](/Images/Diagram 4.png "Diagram 4")
![Diagram 5](/Images/Diagram 5.png "Diagram 5")
![Diagram 6](/Images/Diagram 6.png "Diagram 6")
![Diagram 7](/Images/Diagram 7.png "Diagram 7")


