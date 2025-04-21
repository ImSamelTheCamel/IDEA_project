# IDE-AI-nator High-Level Design

## IDE-AI-nator
The IDE-AI-Nator is a web application designed to revolutionize the way Utah State University proessors and administrators interact with and analyze student feedback from IDEA surveys. This AI-powered tool seamlessly integrates with USU's existing systems, offereng a user-friendly interface for accessing, processing, and deriving insights from course evaluations. Some key features include:
- Secure Authentication using USU's Microsoft 2FA
- AI analysis of student feedback using ChatGPT
- Role-based access control for different levels of university staff

The system prioritizes security, user experince, and efficient data processing, with the goal of providing actionable feedback to professors that can improve teching methods and overall course quality.

## Security
- Introduction
   - The security part of this document describes and outlines the lengths gone by the development team to create a secure and safe software for instructors at Utah State University to use without doubt or hesitation. The sections of the security section will outline the efforts taken to secure the application. This is a living document that will be updated and changed as developments happen and decisions are made.

- Data Categories:
   - Sensitive Data (Encryption required)
      - User Login information
      - Pdf files (including student information)
      - AI processing results
      - Login attempts and number of pdfs processed
      - User Queries
      - User information (Position)
   - Non-Sensitive Data (Encryption not required)
      - User Department
      - User's classes (Already public information)

- Data Encryption
   - Storage Encryption: The program will not be storing sensitive information for long periods of time, between sessions pdfs and other documents will not be saved, so storage encryption is not necessary. 

   - Transmission Encryption: The application will provide a safe means for transfering data from the user's local computer to the plugin for processing. End to End encryption will be used to ensure the secure transfer of files from one location to antoher and delivery to endpoints.

- Access Control
   - Authentication: The plugin will use Microsoft Two Factor Authenticator already used by the university. This will provide a familiar means to accessing the software that will be secure but not confusing for the users. 

   - Authorization: RBAC (Role-Based Access Control) will be used to ensure only authorized personel can access certain portions of the information. 
      - Levels of authorication: Instructor (can view own information), Department Head (can view own information and information of instructors in department), Head of University (can access information university wide), Administrator (can access all information) 

- Data Masking/Anonymization:
   - Student information will be anonymized before being given to the system, preventing instructor targeting or preconcieved notions swaying the results. 

- Audit logging - NOT IMPLEMENTED
   - The program will keep a detailed log of logins, pdf files uploaded, queries, pdf files downloaded, logouts. This logs will be timestamped and kept secure and tamper-resistant to provide a means for administrators to show results and usage of the program. 


- Data Retention and Deletion
   - Data retention and deletion will follow the laws of FERPA to ensure the safety of student's information while still providing a useful service to instructors and administrators. The survey's will not be saved on the system, however qiries will be saved and used for collection of data of usage. 

- Input Validation and Threat Prevention
   - Different methods will be used to ensure proper usage of the pdf input and also the quiery system. Data and File type validation will be used to ensure the proper input of only pdf files and string quieries. Length validation will be used to ensure the files or quieries will not cause problems on the system with too long files or quieries. Escaping special characters that could be interpreted as code to prevent injection attacks, we want to control how the system is used in the scrubbing of files. 
    - Session tokens will be used to protect the site Cross-Site request forgery and other attacks. 
    - Rate limiting will be used to prevent brute force attacks to cause damage to the system.
    - Detailed error messages will not be shown to the user, and proper error handling will ensure secure usage.
    - Using prepared statements or parameterized quieries to prevent attackers from SQl injections.

- Incident Response
   - Procedures will be created to ensure the proper identification, reporting, and reponse to any issue that arrises in the application. This includes the inevitable security breach or unauthorized access. The response will be fast and prepared. 

- Regular Security Audits
   - Security will be continuously monitored to ensure the proper updating of security measures. Test attacks will be used periodically to keep the development team informed and to propely ensure the safety of our users and their information. 

- Secure Software Development Practices
   - During the development process, secure practices will be used to keep the code and data used up to the proper standards. Code reviews will be used and no piece of code will only have one set of eyes on it before being published or added to the program. Secure libraries will be used and ensured that the outside code added to the system is safe. 

## Hardware Platform
- **Chosen Platforms**: 
  - **Platform 1**: **Internet Browser** on **Desktop/Laptops**  
    The IDE-AI-Nator will be designed as a web app. This hardware choice allows for a larger display area, which influences the design to include detailed interactions and a clean, spacious UI. It will also ensure compatibility with multiple operating systems (Windows, macOS, Linux). The design will prioritize ease of access and readability, ensuring that all interface elements remain intuitive and efficient in smaller resolutions.

- **User Interface Considerations**:
  - The user interface (UI) will be modern and intuitive, focusing on simplicity and ease of use for a seamless experience. The extension will follow the **Utah State University** branding guidelines, utilizing official school colors as specified in the [USU Branding Toolkit](https://www.usu.edu/brand/toolkit/guides/colors). Key elements will include intuitive flow, minimalistic design, and easy-to-navigate controls, all contributing to a user-friendly experience. Above all things, simplicity is key because many users of IDE-AI-Nator will be of all ages and technological backgrounds.

## Internal Interfaces
- **System Components**: 
  User Interface (UI) – Handles user interactions and inputs.
  AI Processing Engine (Ide-AI-nator) – Analyzes and summarizes feedback using AI-driven algorithms.
  Feedback Database – Stores raw and processed feedback data securely.
  Authentication & Authorization Module – Manages user identity, Single Sign-On (SSO), and permissions.
  Encryption Module – Ensures secure data transmission and storage.
  Session Manager – Maintains user sessions, enabling session-based operations.
  Admin Console – Allows system admins to manage and monitor user roles, feedback summaries, and trends.

- **Internal Interactions**: 
  - Data Flow: 
    UI → AI Processing Engine: User feedback is passed from the UI to the AI engine for analysis.
    AI Processing Engine → Feedback Database: After processing, feedback data and AI summaries are saved in the  database.
    Authentication & Authorization Module ↔ UI: Handles login, user validation, and SSO across various components.
    Encryption Module: Data passing between all components is encrypted, ensuring secure communication.

  - Control Mechanisms: 
    Event-driven: The system will use event-based control mechanisms. For example:
      User submits feedback (triggers AI Processing).
      Admin makes changes (triggers updates across modules).
      Sessions expiring (trigger automatic logouts and save user state).

  - Protocols: 
    REST APIs: The system will use RESTful APIs for communication between components (e.g., AI engine and feedback database).
    OAuth 2.0: For secure SSO and user authentication across different components.
    HTTPS: All data exchanges will be encrypted using HTTPS to ensure security.
    
- **Justifications**: 
  Modular Components: Each component is well-defined, allowing for easy maintenance. Future upgrades to individual components (e.g., upgrading the AI engine) can be done with minimal disruption to the rest of the system.
  Event-driven Architecture: This simplifies control flow, making debugging easier by isolating events and tracing errors to specific triggers.
  REST APIs: Using standardized APIs promotes flexibility and scalability, making it easier to debug and maintain individual services.
  OAuth 2.0 and HTTPS: These protocols ensure secure communication and reduce potential security vulnerabilities, simplifying future troubleshooting efforts related to data breaches.

- **2 Factor Authentication**:
  - The user will be able to log in using the USU incorporated Microsoft 2 Factor Authentication (2FA). In order to access their IDEA surveys in the USU database, Users will be required to verify their identity. 
  - **Application Registration in Azure AD:** The process begins with registering the application in Azure Active Directory (Azure AD), which provides necessary credentials like client ID and tenant ID for authentication integration.
  - **Multi-Factor Authentication Setup:** Multi-factor authentication (MFA) is enabled for users within Azure AD. This can involve methods such as the Microsoft Authenticator app, SMS, or phone calls, adding a layer of security beyond passwords.
  - **Integration with MSAL (Microsoft Authentication Library):** The application needs to integrate the Microsoft Authentication Library (MSAL) to manage authentication requests and token handling. MSAL helps obtain access tokens required for accessing resources, including the MFA challenge.
  - **Prototyping Authentication Flow:** Once the app is integrated with MSAL, the user is prompted to authenticate through MFA during the sign-in process. The application manages token validation, refreshing, and ensuring secure access.
  - **Security Layers and Risks:** Integrating 2FA enhances security by requiring users to verify their identity through multiple channels. However, care must be taken to manage stakeholder expectations and ensure users are aware of the 2FA process and its impact on user experience.

## External Interfaces
The IDE-AI-nator uses several external systems to ensure a quality and secure user experience. These interfaces enable the application to retreive necessary data, authenticate users, process information, and present results effectively. By integrating with exisitng system and using AI, the IDE-AI-nator can efficiely analyze and provide insights from student feedback. This section outlines the ChatGPT AI model integration

**ChatGPT AI Model**
- Purpose: The IDE-AI-nator will use ChatGPT, a large language model, to analyze student feedback and generate a useful analysis with actionalable items for professors and administrators. 
- Functionality:
  - Text Processing: ChatGPT will analyze student feedback, identify key themes, and generate summarized reports, highlighting things the professor has done well and areas of improvement based on the povided student feedback
  - User Interaction: Users will be able to ask questions to the model regarding their feedback and ChatGPT will respond with revant information. An example question might be "What were the most common complaints from this semester?"
  - Custom Responses: ChatGPT will be trained tot ailor its responses to the educational context, ensuring that its feedback is directly applicabe to university instructors and administrators
- Input/Output:
  - Inputs: Student feedback data and natural language queries from instructors
  - Outputs: AI-Generated feedback summaries and analysis, insights based on user queries
- Security Considerations:
  - ChatGPT will process all data in a secure environment, data sent to the model will be encrypted.
  - ChatGPT will not store any student information to be compliant with FERPA regulations
  - Chat histoy will be saved using ChatGPTs converstion storing methods.

## Prototypes

### Prototyping Strategy:
#### Low-Fidelity Prototypes: 
Low-fidelity prototypes will be used during the early stages of design to quickly visualize the concept, test the flow of the system, and gather initial feedback from Nate. These prototypes will be basic digital mockups that focus on overall structure and functionality rather than detailed design. Low-fidelity prototypes will allow us to:
- Quickly iterate on ideas without heavy investment in time or resources.
- Facilitate discussions and validate the main concepts with stakeholders early on.
- Identify and resolve major design flaws before moving into more detailed development.

#### High-Fidelity Prototypes: 
High-fidelity prototypes will be introduced once the core design and functionality are agreed upon through low-fidelity feedback. These will include near-production designs that mimic the look, feel, and interactivity of the final product. High-fidelity prototypes will:
- Allow for detailed usability testing.
- Provide a clearer representation of the user interface (UI), including branding, color schemes, and interactivity.
- Help developers understand specific requirements for implementation.

High-fidelity prototypes will be developed before final design sign-off and prior to major development milestones to reduce the gap between design and code.

### Risks of Overdeveloped Prototypes:
Overdeveloping prototypes can lead to unrealistic stakeholder expectations, as they may perceive the prototype to be near-final even though it is not functional. This can cause disappointment if the final product takes longer to develop or looks slightly different.

#### Risk Management Strategies:
- Set clear expectations with stakeholders by emphasizing that prototypes, especially high-fidelity ones, are not fully functional but are meant to guide the development process.
- Maintain transparency about what the prototypes represent in terms of functionality and timeline.
- Regularly communicate the purpose and limitations of the prototypes during meetings.

### Benefits:
Iterative development with prototypes ensures that design and functionality are aligned with user needs and business requirements from the start. Key benefits include:
- **User Feedback**: Incorporating user feedback during the prototyping phase allows for adjustments before large development efforts are made, reducing the need for costly changes later.
- **Improved Design**: By testing different iterations, we can fine-tune the product for better usability, ensuring a more user-friendly experience in the final version.
- **Risk Reduction**: Early prototypes help identify potential design flaws, performance bottlenecks, and usability issues early, leading to a smoother development process.

## Performance Requirements
To ensure the IDE-AI-nator meets user expectations and operates efficiently, the following performance requirement shsould be met:

**Response Time**
- User Interface: The Chrome extension should load within 2 seconds of actviation
- Data Retrieval: Course feedback data should be retrieved from USU Campus Labs within 5 seconds of a request
- AI Processing: ChatGPT should generate responses withing 3-5 seconds

**Throughput**
- The system should hadnle at least 1000 concurrent users during peak perids
- AI processing capabilities should spport analysis of at least 100 feedback submissions per minute

**Scalability**
- The architecture should allow for a 50% increase in user base whtout significant performance degradation
- The system should be able to scale hoizontally to accommodate growing data processing needs

**Availability**
- The IDE-AI-nator should maintain 99.9% uptime during semesters
- planned maintenance should be scheduled at times when there is the least activity to minimize disruption

**Resource Utilization**
- The Chrome extension should use no more than 100 MB of memory on the clients browser
- Server-side processes should optimize CPU and memory usage to ensure cost-effective operation

**Load Handling**
- The system should handle sudden spikes in traffic, up to 200% of the normal load, without crashing

**Data Processing**
- bulk uploads of feedback data should be processed within 1 hour for up to 10,000 suybmissions. In this case it is acceptable for ChatGPT to take longer than 3-5 seconds to process the data and generate a response

## Input and Output Considerations
- **Inputs**: 
  - Real-time data: User feedback, rating submissions, and suggestions from students
  - API Requests: Data from third-party integrations for SSO, security checks, and ChatGPT AI
  - User interactions: Inputs from different user roles(proffesors, head of department, dean, etc)
  - File uploads: Possible input of document files for bulk feedback submissions or report generation

- **Architectural Choices**: 
  - Data Flow Management: Real-time inputs will require efficient processing and queuing mechanisms, ensuring low latency feedback
  - API Integration layer: A well-structured middleware will handle external requests securely
  - Authentication+Security: SSO inputs need to pass through secure Authentication systems, impacting network design and session management 
  - Scalability: System must handle spikes in real-time during peak usage

- **Outputs**: 
  -Reports: AI-generated summaries of feedback, detailed analytics on trends, and system-generated suggestions
  -Logs: Detailed logs of system usage, input data processing, and feedback AI analysis outcomes for audit and debugging purposes
 - **Architectural Considerations**: 
    Scalability & Performance: A distributed architecture will be employed to manage the high volume of outputs (e.g., reports, dashboards) generated simultaneously. This will allow the system to distribute the workload across multiple nodes, ensuring high performance and availability.
    Security & Compliance: Robust security measures, such as encryption and access control, will ensure that sensitive reports and logs are only accessible to authorized users. The system will also implement audit trails to track user access and actions within the system.
    Flexibility & Extensibility: The architecture will allow for future expansion, supporting additional input types or output formats as needed. This includes integrating new third-party APIs or scaling the reporting and analytics components.
    Real-time Notifications: An event-driven architecture will handle real-time notifications and alerts, enabling the system to respond quickly to critical conditions or events and send notifications to relevant users as needed.
  

## Reports
#### **Types of Reports**  

The **IDE-AI-nator** will generate a variety of reports tailored to different user roles and needs, ensuring that stakeholders can efficiently access, analyze, and act on student feedback. These reports aim to provide actionable insights into teaching effectiveness, performance trends, and areas for improvement.

- **Feedback Summary Reports**
  - **Overview**: This report provides a concise summary of student evaluations, highlighting key feedback metrics such as overall instructor effectiveness, course content satisfaction, and classroom environment. 
  - **Frequency**: Automatically generated at the conclusion of each evaluation period.
  - **Advantages**:
    - Empowers instructors to quickly assess student sentiment and identify areas needing improvement.
    - Facilitates oversight for department heads by offering a transparent view of course performance.
    - Features visual aids such as charts and graphs for easy comprehension of key metrics.

- **On-Demand Reports**
  - **Overview**: Users can generate specific reports at any time by applying filters based on criteria such as course, instructor, department, or time frame.
  - **Format**: Customizable reports that can be exported in various formats, including PDF and Excel.
  - **Advantages**:
    - Provides stakeholders with flexibility to obtain specific insights as needed.
    - Facilitates informed decision-making by granting timely access to pertinent data.

- **Archiving & Retrieval**
  - **Overview**: Implement an archiving system for past reports to provide a long-term view of performance data.
  - **Details**:
    - Archived reports will be easily retrievable for future reference or analysis.

- **Stakeholders**
  - **Instructors**: Access their own course feedback and trend reports to inform teaching practices and engage with student concerns.
  - **Department Heads**: View summary and trend analysis reports for all courses within their department, facilitating strategic decisions and faculty development.
  - **Head of University**: Access comprehensive reports that aggregate data across all departments to evaluate institutional performance and teaching quality.
  - **Administrators**: Manage access and oversee the integrity of the reporting system, ensuring compliance with data protection regulations.
  - **Students**: Have limited access to aggregated feedback summaries, promoting transparency while maintaining the confidentiality of individual responses.


## UML Diagrams
- https://www.canva.com/design/DAGQZmUuwsQ/8hw8ppszUCfN3digUK6eLg/edit
  
