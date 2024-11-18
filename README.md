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
   - Admin authentication system
   - Virtual environment support

2. **File Structure**
```
cloud-resume-azure/
├── frontend/
│   ├── admin/
│   │   ├── manage_resume.py     # Main management interface
│   │   ├── update_roles.py      # Role management system
│   │   └── update_projects.py   # Project management system
│   ├── data/
│   │   ├── roles.json           # Role data storage
│   │   └── projects.json        # Project data storage
│   ├── js/
│   │   └── work-toggle.js       # Public interface JavaScript
│   ├── index_template.html      # Template for generation
│   └── index.html              # Generated website
├── venv/                       # Python virtual environment
└── requirements.txt            # Python dependencies
```

### Next Steps
1. Complete Azure infrastructure setup
2. Implement visitor counter
3. Configure CI/CD pipeline
4. Add more roles and projects data

## Setup Instructions

### Local Development Setup
1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd cloud-resume-azure
   ```

2. Set up Python virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   pip install -r requirements.txt
   ```

3. Initialize the admin system:
   ```bash
   cd frontend/admin
   python manage_resume.py
   ```
   - Follow the prompts to set up your admin password
   - Use the management interface to add/edit roles and projects

### File Structure Details
- **index_template.html**: Base template for the resume website
- **index.html**: Generated website with actual content
- **roles.json**: Stores role information in categories (Administrative, Clinical, Academic)
- **manage_resume.py**: Main interface for content management

## Architecture Overview

### 1. Local Management System
- **Role Management System**
  - Python-based content management
  - JSON data storage for role information
  - HTML template generation
  - Admin authentication
  - Features:
    * Add/remove/update roles
    * Generate formatted HTML
    * Maintain career history
    * Category-based organization (Clinical, Administrative, Academic)
    * Toggle between categorized and chronological views

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
  - Virtual environment for dependency management

- **Frontend**
  - HTML5/CSS3
  - Modern JavaScript
  - Responsive design
  - Category/chronological view toggle

- **Cloud Services**
  - Azure Blob Storage
  - Azure Functions
  - Azure CosmosDB
  - Azure CDN (optional)

- **DevOps**
  - GitHub
  - GitHub Actions

## Resources
- [Azure Static Website Documentation](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website)
- [Azure Functions Python](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [Azure CosmosDB](https://docs.microsoft.com/en-us/azure/cosmos-db/)

## Project Status
- ✅ Local management system implemented
- ✅ Role management system completed
- ✅ Admin authentication added
- ✅ Virtual environment setup
- ⏳ Azure infrastructure setup in progress
- ⏳ Visitor counter implementation pending
- ⏳ CI/CD pipeline configuration pending
