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
   - Azure Cosmos DB
   - Stores visitor count data
   - Connected to Azure Function

### Deployment Strategy
- **Frontend Updates**: Using Azure Storage Explorer
- **Backend Updates**: Using Local Git deployment
- **Version Control**: GitHub repository backup
- Note: GitHub Actions workflows are currently disabled for manual deployment control

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
```
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

## Recent Updates (2024-01-20)
1. **Deployment Changes**
   - Disabled GitHub Actions workflows
   - Switched to manual deployment control
   - Set up GitHub Desktop for repository management

2. **Development Environment**
   - Using Azure Portal for frontend updates (temporary)
   - Planning to set up Storage Explorer once .NET 8 is properly installed
   - GitHub Desktop configured for version control

3. **Known Issues**
   - Need to review `frontend/main.js` for potential duplicate file issue
   - Verify correct JavaScript file being used (`frontend/js/resume.js` vs `frontend/main.js`)
   - Ensure proper file organization in frontend directory

## Next Steps
1. **Tools Setup**
   - Install .NET 8 Runtime
   - Install Azure Storage Explorer
   - Configure VS Code for function updates

2. **Code Review**
   - Review and resolve main.js file location/usage
   - Ensure correct JavaScript file is referenced in index.html
   - Clean up any duplicate JavaScript files

3. **Testing**
   - Verify frontend update process via Azure Portal
   - Test visitor counter functionality
   - Confirm GitHub backup process

4. **Future Updates**
   - Plan new feature additions
   - Update content as needed
   - Enhance interactive elements

## Live URLs
- Website: [www.troymd.com](https://www.troymd.com)
- Counter API: [resume-counter-function-sybert.azurewebsites.net/api/GetResumeCounter]
