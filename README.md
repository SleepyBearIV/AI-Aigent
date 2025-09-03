# AI Aigent - LLM Chat Interface

A Python-based chat interface using FastAPI backend with LM Studio integration.

## Prerequisites

### 1. Frontend Application
This backend requires a separate frontend application to function:
- Repository: [AI-Frontend](https://github.com/SleepyBearIV/AI-frontend)
- Follow the installation instructions in the frontend repository
- The frontend will connect to this backend at http://localhost:8000

### 2. LM Studio Installation and Setup
1. Download LM Studio:
   - Go to [https://lmstudio.ai/](https://lmstudio.ai/)
   - Download the appropriate version for your OS
   - Run the installer

2. First-Time Setup in LM Studio:
   - Launch LM Studio
   - Go to "Models" tab
   - Download model:
     * Required model: openai/gpt-oss-20b (this is hardcoded in the system)
     * If you want to use a different model, you'll need to modify chat_client.py
   - After downloading:
     * Select your model
     * Click "Start Server" button
     * Verify server starts on http://localhost:1234

### 2. Python Environment Setup
1. Create a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install required packages:
   ```powershell
   pip install -r requirements.txt
   ```
   
   Dependencies include:
   - python-dotenv (environment variables)
   - aiohttp (async HTTP client)
   - fastapi (API framework)
   - uvicorn (ASGI server)
   - pydantic (data validation)

3. Environment Configuration:
   Create a `.env` file in the src directory:
   ```
   LM_STUDIO_BASE_URL=http://localhost:1234/v1
   TEMPERATURE=0.7
   MAX_TOKENS=2000
   ```

## Starting the System

1. **Start LM Studio First**:
   - Open LM Studio
   - Select your model
   - Click "Start Server"
   - Wait for "Server is running" message

2. **Start the Backend**:
   ```powershell
   cd src
   python -m uvicorn api:app --reload --port 8000
   ```
   
   Backend will be available at:
   - API: http://localhost:8000/chat
   - Docs: http://localhost:8000/docs

## Project Structure
```
AI Aigent/
├── src/
│   ├── api.py          # FastAPI endpoints
│   ├── chat_client.py  # LM Studio client
│   └── agent.py        # Agent implementation
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Troubleshooting

1. **LM Studio Issues**:
   - Ensure enough RAM for your chosen model
   - Check server status in LM Studio UI
   - Verify http://localhost:1234 is accessible

2. **Backend Issues**:
   - Check virtual environment is activated
   - Verify all dependencies installed
   - Ensure port 8000 is free
   - Check .env file exists and is correctly formatted

## Development Resources

- FastAPI Docs: https://fastapi.tiangolo.com/
- LM Studio Docs: https://lmstudio.ai/docs/
- Pydantic Docs: https://docs.pydantic.dev/

## License and Usage Restrictions

**PRIVATE PROJECT - NOT FOR PUBLIC USE**

This is a private project and is not licensed for public use, distribution, or modification. All rights reserved. 
The code, documentation, and all associated materials are proprietary and confidential.

- No public distribution
- No unauthorized copying or modification
- No commercial use
- No sharing or redistribution

Copyright © 2025. All Rights Reserved.