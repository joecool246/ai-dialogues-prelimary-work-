# ai-dialogues-prelimary-work-
Preliminary work over ai dialogues

This is a private repo documenting intial workings with AI Dialogues. More up to date work will be with Purdue's GRAIL Github. Please note that this work is intellectual propertiery and thus not much can be shared on this repo. 

Project Iterations:

v1  # Gemini Debate Bot (CLI)

A **command-line debate application** that lets you debate an AI powered by **Google Gemini**, configured to role-play as a **hardline right-wing / ultra-conservative debate partner**, with strict safety guardrails (no hate, no violence, no extremist praise).

You choose the topic, debate back and forth, and end the session with a stop token.

---

## What This Program Does

- Prompts you for a **debate topic**
- Starts a Gemini chat session with a predefined debate persona
- Alternates turns between **you** and **Gemini**
- Keeps running until you type the stop token
- Prints all responses directly in the terminal

---

## Requirements

### Software
- **Python 3.9+** (3.13 recommended)
- Internet connection

### API Access
- A valid **Gemini API key** (Google AI / Gemini)

---

## Project Files

At minimum, you need:

debate_script.py

## Installation
  1) Create a Virtual Environment (Recommended)
  Windows (PowerShell)
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1

  macOS / Linux (bash/zsh)
  python3 -m venv .venv
  source .venv/bin/activate
  
  2) Install Dependencies
  pip install -U google-genai
  
  
  If that fails, upgrade pip first:
  
  python -m pip install --upgrade pip
  
## API Key Setup
  
  This script requires the API key to be set as an environment variable named:
  
  GEMINI_API_KEY
  
  Windows (PowerShell)
  $env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
  
  macOS / Linux (bash/zsh)
  export GEMINI_API_KEY="YOUR_API_KEY_HERE"
  
  Verify (Optional)
  echo $GEMINI_API_KEY

  If it prints your key, it is set correctly.
  
  ⚠️ Important
  The environment variable must be set in the same terminal session where you run the script.

## Running the Program
  1) Navigate to the project folder
  cd path/to/your/project
  
  2) Run the script
  python debate_script.py
  
  3) When prompted, enter a debate topic
  What topic do you want to debate? abortion
  
  4) Debate naturally
  
  Type responses and press Enter after each message.
  
  5) To end the debate, type
  STOP123
  
  
  The program will exit immediately.
  
  Conversation Flow
  Gemini speaks
  You respond
  Gemini responds
  You respond
  ...
  STOP123 → program ends
  
  Configuration Options (Inside the Code)
  Stop Token
  STOP_TOKEN = "STOP123"
  
  
  Change this if you want a different exit keyword.
  
  Model Selection
  MODEL_ID = "gemini-2.5-flash"
  
  
  You may switch models if others are available to your account.
  
  Response Length
  max_output_tokens = 1600
  
  
  Increase if responses feel cut off
  
  Decrease if responses are too long
  
  Creativity / Aggressiveness
  temperature = 0.8
  
  
  0.3–0.5 → calmer, more rigid arguments
  
  0.7–0.9 → more rhetorical, aggressive debate
  
  >1.0 → less predictable (not recommended)

## Troubleshooting
  ❌ API key expired / API_KEY_INVALID
  
  Make sure your key is correct and active
  
  Re-set the environment variable
  
  Restart the terminal
  
  Ensure there are no extra spaces or quotes
  
  ❌ ModuleNotFoundError: No module named google
  pip install -U google-genai
  
  
  If using a virtual environment, confirm it is activated.
  
  ❌ Responses Look Truncated
  
  Increase max_output_tokens
  
  Widen your terminal window
  
  VS Code may visually wrap long lines — content is still there
  
  ❌ Script Runs but Immediately Exits
  
  You likely pressed Enter without entering a topic
  
  The program exits if the topic is blank
  
  ❌ Environment Variable Not Found
  
  You must set GEMINI_API_KEY every new terminal session
  
  VS Code may need a full restart after setting env vars
  
  Safety & Scope Notes
  
  The AI may argue strongly, but:
  
  No slurs
  
  No violence
  
  No extremist praise
  
  These rules are enforced automatically by the system prompt.
  
  This tool is intended for:
  
  Debate practice
  
  Rhetorical analysis
  
  Civic dialogue exploration
  
  Disclaimer
  
  This project is for educational and experimental use only.
  It does not represent endorsement of any ideology or political position.

