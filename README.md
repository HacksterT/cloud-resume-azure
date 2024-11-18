# Cloud Resume Project

## Project Overview
This project implements a cloud-based resume website with a visitor counter, utilizing various Azure services and modern web technologies. It's based on the Cloud Resume Challenge but modernized and implemented using Python for backend services.

## Architecture Overview

### 1. Frontend Architecture
- **Static Website**
  - HTML, CSS, JavaScript
  - Resume content display
  - Visitor counter integration
  - API integration for counter updates

- **Hosting Options**
  - Azure Blob Storage (with static website hosting)
  - Alternative: Azure Static Web Apps
  - Features:
    * CDN integration capability
    * Custom domain support
    * SSL/TLS encryption

### 2. Backend Architecture (Python-based)
- **Azure Functions**
  - HTTP-triggered functions using Python runtime
  - Python Azure Functions SDK
  - Azure SDK for Python for database interactions
  - Features:
    * RESTful API endpoints
    * CORS configuration
    * Serverless architecture

- **Database: Azure CosmosDB**
  - NoSQL document database
  - Stores visitor counter data
  - Scalable and serverless

### 3. Integration Components
- Frontend ↔ Backend: REST API calls
- Backend ↔ Database: Azure SDK bindings
- GitHub ↔ Azure: Automated deployment

### 4. DevOps Pipeline
- **Source Control**
  - GitHub repository
  - Branch protection rules
  - Code review process

- **CI/CD: GitHub Actions**
  - Automated testing
  - Deployment automation
  - Environment management

- **Testing Framework**
  - pytest for Python backend
  - Integration tests
  - API testing

## Technology Stack
- **Frontend**
  - HTML5
  - CSS3
  - JavaScript (vanilla/modern)

- **Backend**
  - Python 3.x
  - Azure Functions Python runtime
  - Azure SDK for Python

- **Database**
  - Azure CosmosDB
  - NoSQL document structure

- **DevOps**
  - GitHub
  - GitHub Actions
  - Azure CLI

## Development Environment Setup
1. Required Tools:
   - Visual Studio Code
   - Azure CLI
   - Python 3.x
   - Azure Functions Core Tools
   - Git

2. VS Code Extensions:
   - Azure Functions
   - Azure Storage
   - Python
   - Azure Account

## Project Structure
```
cloud_resume/
│
├── frontend/
│   ├── index.html
│   ├── css/
│   └── js/
│
├── backend/
│   ├── counter_function/
│   │   ├── __init__.py
│   │   ├── function.json
│   │   └── requirements.txt
│   └── tests/
│
├── infrastructure/
│   └── terraform/  # or ARM templates
│
└── .github/
    └── workflows/
```

## Security Considerations
- CORS configuration
- Function-level authentication
- Managed Identities for Azure resources
- Key Vault for secrets management

## Deployment Process
1. Frontend deployment to Azure Storage
2. Backend deployment via GitHub Actions
3. Database provisioning and configuration
4. CI/CD pipeline setup

## Testing Strategy
- Unit tests for Python functions
- Integration tests for API endpoints
- End-to-end testing
- Load testing considerations

## Future Enhancements
- CDN integration
- Custom domain setup
- Analytics integration
- Enhanced security features

## Resources and References
- [Azure Functions Python Documentation](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [Azure CosmosDB Python SDK](https://docs.microsoft.com/en-us/azure/cosmos-db/sql/sql-api-python-samples)
- [Azure Static Website Hosting](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Project Status
- Initial setup and documentation phase
- Planning and architecture design
- Ready for implementation

## Notes
- Python-based implementation instead of original C# version
- Modern Azure services integration
- Focus on serverless architecture
- Emphasis on automation and DevOps practices
