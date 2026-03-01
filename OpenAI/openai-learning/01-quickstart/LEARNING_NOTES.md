# Learning Notes - OpenAI Quickstart

## Day: 1

### What I Learned Today
- Setting up OpenAI acoount 
- Creating API and funding the account 
- Setting up Cursor for OpenAI learning 
- Setting up uv - package manager for python 
- Running hello world app (quickstart.py)
- Checking API usage on OpenAI 

### Code That Worked Well
```python
# Paste working code snippets
```

### Challenges I Faced
- Environment setup 
- Issue with Node.js and npm isn’t installed or not on your PATH.
- Issue with python means the python shim isn’t on your PATH. On macOS, the command is usually python3.
- Issue with python and pip aren’t installed/available yet, and on macOS the command is usually python3/pip3.
- Issue with pip isn’t found because only python3 is on your PATH right now, not the unversioned pip shim.

### Gotchas & Mistakes
- Not knowing when to use python vs python3 on Mac
- Learned what is the purpose of .gitignore 

### Questions for Later
- Don't understand how to use global / local settings for .env. venv 
- Don't understand how to use requirements.txt 

### Ideas for Training Material
- There should be setup guide for different environments - Windows/Mac 
- There should be setup for Cursor and OpenAI 

### Student Exercise Ideas
- 
```

### Step 11: Project Structure Overview

Your final structure should look like:
```
01-quickstart/
├── venv/                    # Virtual environment (gitignored)
├── examples/
│   ├── 01_basic_completion.py
│   ├── 02_system_message.py
│   ├── 03_conversation.py
│   └── 04_parameters.py
├── .env                     # Your API key (gitignored)
├── .gitignore
├── quickstart.py           # Main entry point
├── requirements.txt
├── README.md
└── LEARNING_NOTES.md