# Cloud Resume Project

## Project Overview
This project implements a cloud-hosted resume website using Azure Static Web Apps. The design focuses on simplicity, maintainability, and professional presentation.

## Live Website
- Production URL: [www.troymd.com](https://www.troymd.com)
- Azure URL: [jolly-flower-02175240f.5.azurestaticapps.net](https://jolly-flower-02175240f.5.azurestaticapps.net)

## Architecture
- **Frontend**: Static HTML/CSS/JavaScript
- **Hosting**: Azure Static Web Apps
- **Domain**: Custom domain (www.troymd.com) with GoDaddy DNS
- **Deployment**: GitHub Actions CI/CD pipeline

## Current Implementation
### Completed Features
1. **Website Structure and Design**
   - Modern, responsive layout
   - Collapsible sections for better content organization
   - Professional styling with consistent color scheme
   - Mobile-friendly design
   - Optimized section navigation with smooth scrolling
   - Professional profile photo integration

2. **Content Sections**
   - Professional Summary (expanded by default)
   - Work Activity with multiple views:
     - Categorized view (Administrative, Clinical, and Academic)
     - Chronological view
     - Gantt chart summary view
   - Credentials & Certifications
   - Publications/Presentations
   - Volunteer Work/Awards
   - Social Media Integration

3. **Interactive Features**
   - Smart section management (only summary expanded on load)
   - Smooth scrolling navigation
   - Multiple work history views with toggle functionality
   - Interactive Gantt chart with role categorization
   - Hash-based navigation support
   - Collapsible work categories with timeline view
   - Animated transitions for better user experience

4. **Domain & Email Configuration**
   - Custom domain setup with Azure Static Web Apps
   - Maintained email forwarding to iCloud
   - Proper DNS configuration with security records
   - Email authentication (SPF, DKIM) preserved

### File Structure
```
cloud-resume-azure/
├── frontend/
│   ├── index.html              # Main resume page
│   ├── assets/
│   │   └── presentations/      # Presentations and profile photo
│   └── js/                     # JavaScript functionality
├── .github/
│   └── workflows/
│       └── azure-static-web-apps.yml  # CI/CD configuration
└── README.md
```

## Development Approach
1. Direct HTML/CSS implementation for faster development
2. Single-file architecture for easier maintenance
3. Built-in styling without external dependencies
4. Static content for reliable performance
5. Interactive features for better user engagement
6. Automated deployment through GitHub Actions

## Deployment Process
1. **Local Development**
   - Clone the repository
   - Make changes to content
   - Test locally using browser

2. **Automated Deployment**
   - Push changes to main branch
   - GitHub Actions automatically builds and deploys
   - Changes live within minutes

3. **Domain Configuration**
   - Azure Static Web Apps hosts the site
   - Custom domain (www.troymd.com) points to Azure
   - DNS managed through GoDaddy

## Maintenance
To update the resume:
1. Make changes to the relevant sections in `index.html`
2. Test locally to ensure all features work
3. Commit changes to Git
4. Push to main branch - automatic deployment handles the rest

## Next Steps
### Backend Implementation
1. **Azure Functions Setup**
   - Create HTTP-triggered Azure Function
   - Configure CORS settings
   - Set up local development environment
   - Deploy to Azure

2. **Database Integration**
   - Create CosmosDB account
   - Set up database and container
   - Configure Function bindings for CosmosDB
   - Implement counter logic

3. **Visitor Counter Feature**
   - Add counter display to frontend
   - Implement JavaScript API call
   - Connect frontend with Azure Function
   - Test counter functionality

4. **Testing Framework**
   - Set up xUnit testing
   - Create test cases for Azure Function
   - Implement integration tests
   - Add tests to CI/CD pipeline

### Resources
- [HTTP triggered Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger)
- [CosmosDB Bindings](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2)
- [xUnit Testing](https://xunit.net/docs/getting-started)
- [JavaScript API Calls](https://www.digitalocean.com/community/tutorials/how-to-use-the-javascript-fetch-api-to-get-data)

## Status
- ✅ Basic structure and styling complete
- ✅ Responsive design implemented
- ✅ Section navigation optimized
- ✅ Content organization finalized
- ✅ Azure deployment complete
- ✅ Custom domain configured
- ✅ Email services preserved
- ✅ CI/CD pipeline established
