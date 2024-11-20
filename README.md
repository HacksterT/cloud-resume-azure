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

## Recent Updates
- Fixed Work Activity section behavior:
  - Now starts collapsed by default
  - Properly toggles open/close when clicked
  - Maintains consistent behavior with other sections
  - Preserved menu functionality for different views (Categorized/Chronological/Summary)
- Simplified JavaScript code for better maintainability
- Removed unnecessary special case handling

## Next Steps
### Backend Implementation (Priority Order)
1. **Visitor Counter Implementation**
   - Create Azure Function API
   - Set up CosmosDB for storing visit count
   - Add counter display to frontend
   - Implement counter increment logic

2. **Azure Infrastructure Improvements**
   - Set up staging environment
   - Implement A/B testing capability
   - Add application monitoring
   - Configure automated backups

3. **Performance Optimization**
   - Implement CDN for static assets
   - Add caching headers
   - Optimize image delivery
   - Implement lazy loading for images

4. **Security Enhancements**
   - Add WAF (Web Application Firewall)
   - Implement rate limiting
   - Set up security monitoring
   - Configure automated security scanning

### To Deploy Latest Changes
1. Commit changes to Git:
   ```bash
   git add .
   git commit -m "Fixed Work Activity section behavior and updated README"
   git push origin main
   ```
2. GitHub Actions will automatically:
   - Build the project
   - Deploy to Azure Static Web Apps
   - Update the live site at www.troymd.com

## Known Issues and Future Work

### Work Activity View Issues
- **Chronological View Not Opening**
  - Issue: While fixing the categorized view collapse/expand behavior, the chronological view stopped working
  - Potential fixes to investigate:
    1. Check if the view toggle event listeners are properly handling the chronological view class changes
    2. Verify the interaction between section collapse state and view changes
    3. Review if the 'active' class is being properly toggled for chronological view
    4. Ensure the view-chronological div structure matches the categorized view
  - Files to check:
    - `frontend/index.html`: Review JavaScript event handlers for view toggles
    - Look specifically at the radio button change handlers
    - Check CSS classes for view-chronological elements

### Visual Design Improvements
- Update chronological view color scheme:
  - Current colors may confuse users as they differ from categorized and summary views
  - Replace current colors with shades of gray to maintain visual distinction without implying category relationships
  - Ensure consistency with the overall design language of the resume

### Overlapping Roles Display
Currently working on improving how overlapping roles are displayed in the chronological view:
- Need to fix the continuation entries to consistently show:
  - Full role title
  - Company name and location
  - Properly formatted date range (Start - End)
  - "(continued)" indicator
- Current implementation only partially works:
  - Some entries are missing company information
  - Date formatting needs to be consistent across all entries
  - Need to ensure proper handling of entries without specific months
- Next steps:
  - Review and fix the continuation entry cloning logic
  - Ensure consistent date formatting
  - Maintain full company information in continuation entries
  - Test across all time periods

## Status
- ✅ Basic structure and styling complete
- ✅ Responsive design implemented
- ✅ Section navigation optimized
- ✅ Content organization finalized
- ✅ Azure deployment complete
- ✅ Custom domain configured
- ✅ Email services preserved
- ✅ CI/CD pipeline established
