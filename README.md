# Cloud Resume Project

## Project Overview
This project implements a cloud-based resume website with a sophisticated content management system and visitor counter. It combines local management tools with Azure cloud services to create a professional, maintainable portfolio website.

## Current Progress
### Completed Features
1. **Content Management System**
   - Created unified management script (`manage_resume.py`)
   - Role management system (`update_roles.py`)
   - Project management system (`update_projects.py`)
   - JSON-based data storage
   - Interactive CLI interfaces

2. **File Structure**
```
cloud-resume-azure/
├── frontend/
│   ├── data/
│   │   ├── roles.json           # Role data storage
│   │   └── projects.json        # Project data storage
│   ├── scripts/
│   │   ├── manage_resume.py     # Main management interface
│   │   ├── update_roles.py      # Role management system
│   │   └── update_projects.py   # Project management system
│   ├── js/
│   │   └── work-toggle.js       # Public interface JavaScript
│   ├── index_template.html      # Template for generation
│   └── index.html              # Generated website
```

### Next Steps
1. Test management systems with real data
2. Set up Azure infrastructure
3. Implement visitor counter
4. Configure CI/CD pipeline

## Architecture Overview

### 1. Local Management System
- **Role Management System**
  - Python-based content management
  - JSON data storage for role information
  - HTML template generation
  - Features:
    * Add/remove/update roles
    * Generate formatted HTML
    * Maintain career history
    * Category-based organization (Clinical, Administrative, Academic)

### 2. Public Cloud Infrastructure
- **Frontend (Azure Static Website)**
  - Generated HTML, CSS, JavaScript
  - Professional portfolio display
  - Visitor counter integration
  - Hosted on Azure Blob Storage
  - Features:
    * CDN integration
    * Custom domain support
    * SSL/TLS encryption

- **Backend Services**
  - Azure Functions (Python-based)
    * Visitor counter endpoint
    * Simple API for public features
  - CosmosDB
    * Store visitor statistics
    * Basic analytics data

### 3. Workflow Architecture
```
Local Management:
Role Manager (Python) → roles.json → HTML Generation → Deploy to Azure
                                                          ↓
Public Access:                                    Azure Blob Storage
                                                          ↓
                                                    Visitor Views
                                                          ↓
                                                Azure Function Counter
```

## Technology Stack
- **Local Management**
  - Python 3.x
  - JSON for data storage
  - Template-based HTML generation

- **Frontend**
  - HTML5/CSS3
  - Modern JavaScript
  - Responsive design

- **Cloud Services**
  - Azure Blob Storage
  - Azure Functions
  - Azure CosmosDB
  - Azure CDN (optional)

- **DevOps**
  - GitHub
  - GitHub Actions
  - Azure CLI

## Project Structure
```
cloud-resume-azure/
├── frontend/
│   ├── data/
│   │   └── roles.json           # Role data storage
│   ├── scripts/
│   │   └── update_roles.py      # Role management system
│   ├── js/
│   │   └── work-toggle.js       # Public interface JavaScript
│   ├── index_template.html      # Template for generation
│   └── index.html              # Generated website
│
├── backend/
│   └── counter_function/        # Visitor counter Azure Function
│
└── infrastructure/
    └── azure/                   # Azure configuration
```

## Development Workflow
1. **Content Management (Local)**
   - Use Python scripts to manage roles
   - Generate new HTML from templates
   - Test locally before deployment

2. **Deployment Process**
   - Deploy static content to Azure
   - Update Azure Functions if needed
   - Verify public access

3. **Monitoring**
   - Track visitor statistics
   - Monitor Azure resources
   - Verify content updates

## Security Considerations
- Local management tools run only on admin machine
- Azure Function security for counter
- CORS configuration for API
- SSL/TLS for all public endpoints

## Future Enhancements
- Enhanced analytics
- PDF resume generation
- Additional interactive features
- Blog integration possibility

## Getting Started
1. **Local Setup**
   - Clone repository
   - Install Python requirements
   - Configure Azure CLI

2. **Azure Configuration**
   - Set up Blob Storage
   - Deploy Azure Functions
   - Configure CosmosDB

3. **Content Management**
   - Use role management scripts
   - Update templates as needed
   - Deploy changes

## Resources
- [Azure Static Website Documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website)
- [Azure Functions Python](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [Azure CosmosDB](https://docs.microsoft.com/en-us/azure/cosmos-db/)

## Project Status
- ✅ Content Management System
  - ✅ Role management
  - ✅ Project management
  - ✅ Main management interface
- ✅ Data storage structure
- ✅ HTML generation
- ⏳ Content population
- ⏳ Azure deployment
- ⏳ Visitor counter
- ⏳ CI/CD pipeline
