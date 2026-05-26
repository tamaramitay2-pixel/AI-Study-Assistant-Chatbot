
# Learning Assistant Chatbot

An AI-powered interactive learning assistant built with Python and OpenAI. This application engages users in a guided, Socratic dialogue to assess their understanding of specific technical or academic topics, subsequently generating a structured learning analysis and mastery report.

## Features

- **Socratic Guidance:** The bot uses leading questions to help users articulate their knowledge and build confidence, rather than just providing direct answers.
- **Structured Data Evaluation:** Leverages OpenAI's Structured Outputs (`beta.chat.completions.parse`) mapped to a strict **Pydantic** model to ensure consistent, reliable schema generation for final reporting.
- **Session Summarization:** Provides an automated, clear breakdown of topics covered, gaps to address, improvement tips, and personalized next steps.

---

## Technical Stack

- **Language:** Python 3.x
- **AI Engine:** OpenAI API (`gpt-4o-mini`)
- **Data Validation:** Pydantic (v2)

---

## Architecture & Code Overview

The system is encapsulated within a modular structure utilizing Pydantic for data contract enforcement:

### 1. Data Schema (`LearningAnalysis`)
Defines the strong-typed contract expected from the OpenAI API upon session completion:
- `subject_covered` (str): Automated detection of the discussion topic.
- `mastery_score` (int): A rating scale evaluating user knowledge.
- `gaps_identified` (List[str]): Areas where the student's understanding requires further reinforcement.
- `tips_for_improvement` (List[str]): Actionable suggestions for self-improvement.
- `next_recommended_topic` (str): Logical next step in the learning trajectory.

### 2. Conversational Engine (`start_bot`)
- Maintains conversational memory utilizing a dynamic message history list.
- Implements robust error handling during API streaming to prevent runtime crashes.
- Evaluates the final session summary deterministically once the user inputs the trigger phrase `"finish"`.

---

## Getting Started

### Prerequisites
Ensure you have an OpenAI API Key.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/learning-assistant-chatbot.git](https://github.com/your-username/learning-assistant-chatbot.git)
   cd learning-assistant-chatbot
Install dependencies:
Make sure you have the required libraries installed:

Bash
pip install openai pydantic
Set up Environment Variables:
Configure your OpenAI API key in your system environment:

Windows (PowerShell):

PowerShell
$env:OPENAI_API_KEY="your_api_key_here"
Linux / macOS:

Bash
export OPENAI_API_KEY="your_api_key_here"
Running the Application
Execute the script from your terminal:

Bash
python main.py
Example Usage & Output
Plaintext
--- Learning Analysis Bot Started ---
Instructions: Chat with the bot. When you're done, type 'finish' to get your report.

You: I want to learn about a list, a tuple, and a dictionary and the difference between them in Python.
Bot: It's wonderful to hear that you are eager to learn about lists, tuples, and dictionaries in Python! ...
...

You: finish

--- Analyzing your learning session... ---

SESSION SUMMARY
Subject: Lists, Tuples, and Dictionaries in Python
Mastery Level: 8/10
Gaps to Address: Distinction between accessing elements in lists/tuples and dictionaries, Understanding use cases for each data structure
Learning Tips: Practice creating and manipulating lists, tuples, and dictionaries on a coding platform., Explore scenarios where each type of structure would be most beneficial.
Next Topic: Nested data structures in Python
