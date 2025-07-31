# 🧠 QuestMasterAI

**QuestMasterAI** is a two-phase system designed to assist authors in creating interactive narrative experiences. By combining classical planning (via PDDL) with generative AI (LLMs), it ensures the creation of rich, logically consistent quests that can be played interactively in a web interface.

---

## 🏗️ Two-Phase Architecture

### 📘 Phase 1: Story Generation

- **Objective**: Transform a narrative idea into a validated PDDL planning problem.
- **Input**:
  - Lore file containing:
    - Quest description
    - Initial state and goal
    - Obstacles
    - Branching factor
    - Depth constraints
- **Process**:
  - Generate annotated PDDL domain and problem files.
  - Validate logical consistency using the Fast Downward planner.
  - If invalid, an LLM-powered Reflection Agent assists the user in refining the story logic.
- **Output**:
  - Validated `domain.pddl` and `problem.pddl`
  - Updated lore (if applicable)

### 🎮 Phase 2: Interactive Story Game

- **Objective**: Convert the validated story into a playable HTML-based experience.
- **Features**:
  - Web interface for interactive storytelling
  - LLM-generated state-specific HTML content
  - Optional image generation for scenes

---

## ⚙️ Tech Stack

- **Programming Language**: Python
- **Web Interface**: Streamlit
- **Planning Engine**: [Fast Downward](https://www.fast-downward.org/)
- **LLMs**: Configurable via `.env`:
  - **Gemini API** (default)
  - **Ollama** (local LLM option)

---

## 🔐 Environment Configuration

The `.env` file is already included in the project root.  
To enable integration with local or external models (Google Gemini, Ollama, etc.), simply edit the existing `.env` file and insert your credentials.

### ✅ Edit the following fields inside `.env`:

```env
GOOGLE_API_KEY="<YOUR_GEMINI_API_KEY>"
GOOGLE_MODEL_NAME="<YOUR_GOOGLE_MODEL_NAME>"
OLLAMA_MODEL="<YOUR_OLLAMA_MODEL>"
```
---

# ⚙️ Fast Downward Setup for QuestMasterAI

**QuestMasterAI** uses the [Fast Downward](https://www.fast-downward.org/) classical planner to validate PDDL planning problems. This guide provides step-by-step instructions to install Fast Downward on **Linux/macOS** and **Windows (via WSL)**, and how to configure it for use within the project.



## 🔽 Step-by-Step Installation

### 🐧 Linux / macOS

1. **Clone the Fast Downward repository**:
   ```bash
   git clone https://github.com/aibasel/downward.git
   cd downward
   ```

2. **Install required dependencies**:
   ```bash
   sudo apt update
   sudo apt install cmake g++ python3
   ```

3. **Build Fast Downward**:
   ```bash
   python3 build.py -j2 release
   ```

4. **(Optional) Test the planner**:
   ```bash
   ./fast-downward.py benchmarks/gripper/domain.pddl benchmarks/gripper/prob01.pddl --search "lazy_greedy([ff()], preferred=[ff()])"
   ```



### 🪟 Windows (via WSL)

> ⚠️ Requires [Windows Subsystem for Linux (WSL2)](https://learn.microsoft.com/en-us/windows/wsl/install)

1. **Open WSL and update packages**:
   ```bash
   sudo apt update
   sudo apt install git cmake g++ python3
   ```

2. **Clone and build Fast Downward**:
   ```bash
   git clone https://github.com/aibasel/downward.git
   cd downward
   python3 build.py -j2 release
   ```

3. **(Optional) Run a test**:
   ```bash
   ./fast-downward.py benchmarks/gripper/domain.pddl benchmarks/gripper/prob01.pddl --search "lazy_greedy([ff()], preferred=[ff()])"
   ```
---

## 🗂️ Project Structure
```
│
│
├── data/                    # Data files and assets
│   ├── html/                # HTML examples
│   │
│   ├── img/                 # Images
│   │ 
│   ├── lore/                # Lore and narrative data
│   |
│   ├── pddl/                # PDDL domain and problem definitions
│   │
│   └── story/               # Story JSON data
│
├── pages/                   # Page Streamlit
│   ├── create_story.py
│   └── play_story.py
│
├── src/                     # Main source code
│   ├── agent/               # AI agent modules
│   │   ├── frontend_generator_agent.py
│   │   ├── pddl_generator_agent.py
│   │   ├── reflect_agent.py
│   │   └── story_agent.py
│   └── utils/               # Utility functions
│   │   ├── constant.py
│   │   ├── llm.py
│   │   ├── template_html.py
│   │   └── utils.py
│   │
    ├── phase_1.py           # main function for phase 1
├── .env                     # Environment variables
├── app.py                   # Entry point Application

```

## 🤖 Agent Descriptions

- 🧩 **PDDL Generator Agent**  
  Transforms narrative descriptions into valid PDDL domain and problem models to enable AI planning.

- 🧠 **Reflection Agent**  
  Uses LLM reasoning to detect inconsistencies or logical flaws in the planned story structure and proposes corrections.

- 🖥️ **Frontend Generator Agent**  
  Builds the interactive web interface (e.g., HTML pages) based on the validated story, allowing user interaction.

- 📚 **Story Agent**  
  Coordinates the story flow using lore inputs and ensures that generated narratives remain consistent with world constraints and predefined elements.

---
## ▶️ How to Run the App (Windows - PowerShell)

To run the QuestMasterAI application on a Windows system using PowerShell, follow these steps:

### 1. Open PowerShell

You can open PowerShell from the Start menu or by pressing `Win + X` and selecting **Windows PowerShell** or **Terminal**.

### 2. Navigate to the project directory

Move into the root folder of QuestMasterAI.

```powershell
.\run_application.ps1
```

## 👥 Authors

- **Antonio Pio Francica**  
- **Rocco Pio Vardaro**

This project was developed as part of an initiative focused on AI-driven storytelling and planning. Contributions, feedback, and collaboration are welcome!

---

## 📄 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this software, provided that you include the original copyright and license.

For full license terms, see the [LICENSE](./LICENSE.txt) file.