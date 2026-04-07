# AI UI/UX Feedback Team (ADK)

A multi-agent Google ADK project that reviews landing page screenshots, gives structured UI/UX feedback, and can generate improved design variants.

## What this project does

- Analyzes landing page quality using a structured UI/UX rubric
- Builds a concrete design improvement plan
- Generates improved visual variants from feedback
- Supports iterative edits on previously generated designs

## Agent Architecture

The system uses one coordinator and multiple specialists.

- UIUXFeedbackTeam (root coordinator)
- InfoAgent
- DesignEditor
- AnalysisPipeline (sequential)
  - UICritic
  - DesignStrategist
  - VisualImplementer
- SearchAgent (helper agent for web search context)

Main implementation files:

- agent.py
- tools.py
- __init__.py
- Feedback_Agent/agent.py
- Feedback_Agent/__init__.py

## Project Structure

- .adk/                      ADK local storage artifacts and sessions
- Feedback_Agent/            ADK-discoverable app package wrapper
- agent.py                   Root agent graph and routing
- tools.py                   Image generation and edit tools
- requirements.txt           Python dependencies
- .env                       Local environment variables (ignored by git)
- .gitignore

## Requirements

- Python 3.10+
- A valid Gemini API key
- Windows PowerShell (or your shell of choice)

## Installation

1. Open a terminal in the project root:

   D:/AI_project/Feedback_Agent

2. Create and activate a virtual environment (if needed):

   python -m venv venv
   venv/Scripts/activate

3. Install dependencies:

   pip install -r requirements.txt

## Environment Variables

Create a .env file in the project root with one of the following:

- GOOGLE_API_KEY=your_key_here
- GEMINI_API_KEY=your_key_here

You only need one of them.

## Run the ADK Web UI

Recommended command from the project root:

python -m google.adk.cli web --host 127.0.0.1 --port 8000 .

Then open:

http://127.0.0.1:8000

In the app dropdown, choose Feedback_Agent.

## Usage Flow

1. Select Feedback_Agent in the ADK UI.
2. Upload a landing page screenshot.
3. Ask for analysis (the pipeline runs end-to-end).
4. Ask follow-up edit requests to refine generated outputs.

