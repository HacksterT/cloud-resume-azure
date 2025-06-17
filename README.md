# Cloud Resume Project

## Project Overview

This project implements a cloud-hosted resume website using Azure services. The design focuses on simplicity, maintainability, and professional presentation.

## Architecture

### Components

1. **Frontend**
   - Static HTML/CSS/JavaScript
   - Hosted on Azure Storage
   - Custom domain: [www.troymd.com](https://www.troymd.com)
   - Managed via Azure Storage Explorer

2. **Backend**
   - Azure Functions (Node.js)
   - Visitor counter functionality
   - Endpoint: resume-counter-function-sybert.azurewebsites.net
   - Managed via Local Git deployment

3. **Database**
   - Azure Blob Storage
   - Stores visitor count data
   - Connected to Azure Function

### Deployment Strategy

- **Frontend Updates**: Automated via GitHub Actions workflow
- **Backend Updates**: Using Local Git deployment (backend workflows remain disabled)
- **Version Control**: GitHub repository backup

## Features

1. **Website Content**
   - Professional Summary
   - Work Activity (Administrative, Clinical, and Academic)
   - Credentials & Certifications
   - Publications/Presentations
   - Volunteer Work/Awards
   - Social Media Integration

2. **Interactive Features**
   - Smart section management
   - Multiple work history views
   - Interactive Gantt chart
   - Real-time visitor counter
   - Smooth scrolling navigation
   - Mobile-friendly design

## File Structure

```plaintext
Azure_Resume-new/
├── frontend/
│   ├── index.html          # Main resume page
│   ├── js/                 # JavaScript functionality
│   └── assets/            # Images and presentations
├── backend/
│   └── api/
│       └── GetResumeCounter/  # Visitor counter function
└── README.md
```

## Development Guide

### Frontend Updates

1. Use Azure Storage Explorer
2. Navigate to the `$web` container
3. Upload or modify files as needed
4. Changes are immediately reflected on the website

### Backend Updates

1. Make changes to function code
2. Use Git to deploy:

   ```bash
   git add .
   git commit -m "Your update message"
   git push azure main
   ```

## Recent Updates (2025-06-16)

1. **Deployment Automation**
   - Re-enabled GitHub Actions workflow for frontend
   - Automated deployment to Azure Static Web App
   - Fixed file structure to match Azure Blob Storage requirements

2. **Frontend Improvements**
   - Added line breaks to experience items for better formatting
   - Updated licensure expiration dates
   - Ensured consistent file organization between local and Azure environments
   - Data is not stored int he JSON files but in the HTML directly

3. **Development Workflow**
   - Streamlined git commit process
   - Established consistent deployment pipeline
   - Verified automatic deployment functionality

## Next Steps

1. **Future Enhancements**
   - Consider automating backend deployment
   - Explore additional UI/UX improvements
   - Implement content updates as needed
   - Establish technology portfolio as new content focused on my artifical intelligence work

2. **Code Review**
   - Review and resolve main.js file location/usage
   - Ensure correct JavaScript file is referenced in index.html
   - Clean up any duplicate JavaScript files

3. **Testing**
   - Verify frontend update process via Azure Static Web App
   - Test visitor counter functionality
   - Confirm GitHub backup process

4. **Future Updates**
   - Plan new feature additions
   - Update content as needed
   - Enhance interactive elements

## Technical Innovation Portfolio (In Development)

The Technical Innovation Portfolio is planned as a new section to showcase technical skills and projects. This feature is currently under development in the `feature/tech-portfolio` branch.

### Planned Structure

1. **Primary Organization: By Technology Domain**
   - AI & Machine Learning
   - Data Analytics & Visualization
   - Cloud Architecture & Solutions
   - Programming & Development
   - Digital Transformation

2. **Secondary Organization: Projects Within Each Domain**
   - Each domain will contain specific projects demonstrating expertise
   - Projects will include descriptions, technologies used, and outcomes

3. **Cross-Referencing System**
   - Projects will be tagged to show cross-domain expertise
   - Filtering options will allow viewing by domain or project type/industry

### Local Development Instructions

To preview HTML changes locally without deploying:

1. **Direct Browser Opening**
   - Navigate to the HTML file in File Explorer
   - Right-click and select "Open with" your preferred browser
   - Or drag and drop the file into an open browser window

2. **Using Live Server (VS Code)**
   - Install the "Live Server" extension in VS Code
   - Right-click on the HTML file and select "Open with Live Server"
   - Changes will update in real-time

3. **Simple HTTP Server**
   - Run a Python HTTP server from the project root:

     ```powershell
     cd c:\Users\email\GitHub\Master_Azure\Resume
     python -m http.server
     ```

   - Access at `http://localhost:8000/frontend/index.html`

## Live URLs

- Website: [www.troymd.com](https://www.troymd.com)
- Counter API: [resume-counter-function-sybert.azurewebsites.net/api/GetResumeCounter]
