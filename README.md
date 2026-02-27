# ASSIGNMENT COMPLETION AUTOMATION

**GitHub**: Tony405-spec  
**DockerHub**: tonykenga405  
**Repo**: ASSIGNMENTCOMPLETIONAUTOMATION

Docker-based system that automates KCA university assignments using AI.

## Architecture
- **AI Service**: DeepSeek/ChatGPT integration for answer generation (Tony405-spec)
- **Automation**: Browser automation for portal (cyberghost)
- **File Manager**: Handles downloads/uploads and conversion (cyberghost)
- **Frontend**: Dashboard for monitoring (cyberghost)

## Quick Start
1. Clone this repo
2. Copy .env.example to .env and fill credentials
3. Run docker-compose up --build
4. Access dashboard at http://localhost:3000

## Docker Images
- AI Service: 	onykenga405/assignment-ai-service:latest
- Automation: 	onykenga405/assignment-automation:latest
- File Manager: 	onykenga405/assignment-file-manager:latest
- Frontend: 	onykenga405/assignment-frontend:latest

## Development
- Branch: feature/* → develop → main
- Never commit to main directly
- Always create PRs
