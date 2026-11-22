# Gemini Debate CLI — Early ConvoLab Exploration

**An interactive Python command-line prototype for structured, safety-bounded debate with Google Gemini.**

**Stack:** Python, Google Gen AI SDK.  
**Status:** Early-stage personal experiment, not the production ConvoLab application. The larger team's newer work is maintained separately.

## What I built

- A configurable Gemini debate persona with explicit boundaries around violent, hateful, and extremist content.
- A conversational CLI with a topic prompt, multi-turn chat session, and explicit stop command.
- Environment-variable API-key loading so credentials do not need to be committed.

This repository is a **small API-integration prototype**. It does not implement a full-stack web app, automatic evaluations, or production reliability infrastructure.

## Quick start

```bash
python -m venv .venv
# Activate the environment for your OS
pip install -r requirements.txt
# Set GEMINI_API_KEY in your shell
python debate_script.py
```

The original setup steps and behavior are documented below. A valid Gemini API key and network access are required.

> This prototype is intended for dialogue research and practice. Generated arguments belong to a simulated persona, not an endorsement of those claims. Prompt instructions reduce risk but do **not** guarantee model behavior.

---

## Original project notes

# Gemini Debate CLI — Early ConvoLab Prototype

**Python · Google Gemini API · Persona prompting · Interactive CLI**

This repository documents early experimentation with AI-assisted political dialogue that preceded the more developed [ConvoLab application](https://convolab.us/). It contains an independent command-line prototype, **not the full Purdue GRAIL ConvoLab research platform**. Later collaborative work is maintained separately; confidential or shared GRAIL source code is not reproduced here.

## What this prototype does

- Prompts a user to choose a debate topic.
- Creates a Gemini chat session with a configurable political-debate persona.
- Generates an opening statement and continues turn-by-turn dialogue.
- Ends when the user types `STOP123`.
- Includes prompt guidance and SDK safety settings aimed at avoiding harmful content.

The simulated debate partner has a deliberately assertive conservative persona for dialogue practice; it does not represent the author's political endorsement.

## Run locally

Requires Python, internet access, a Google Gemini API key, and the `google-genai` Python package.

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -U google-genai
```

Set your API key locally — **never commit it to Git**.

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="your-key"
python debate_script.py
```

macOS/Linux:

```bash
export GEMINI_API_KEY="your-key"
python debate_script.py
```

Enter a topic, reply to the AI, and type `STOP123` to exit. The script's model, temperature, output limit, and persona instruction are configurable in [`debate_script.py`](debate_script.py).

## Engineering notes

This proof of concept uses the Google Gen AI SDK, a persistent chat session within one process, a persona-specific system instruction, and a simple interactive input loop.

## Limitations

- CLI-only: no web application, storage, accounts, or multiuser support.
- Requires live model access; generated output can be inaccurate.
- No automated evaluation, dialogue-quality metrics, or reproducible experimental findings.
- Prompt guardrails and provider safety settings **reduce risk but do not guarantee safe behavior**.

## Related work

- [ConvoLab](https://convolab.us/) — more developed collaborative research application.
- [CivicShield AI](https://github.com/joecool246/civicshield-ai) — a separate full-stack civic verification MVP.

**Status:** early experimental prototype for educational use.
