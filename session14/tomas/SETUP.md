# Tomas CrewAI - Setup & Run Guide

Complete step-by-step guide to get your research Flow up and running.

## ✅ What Was Done

Your project has been refactored according to the **CrewAI Quickstart documentation** with the following improvements:

### 1. **Flow Architecture** (Recommended Pattern)

- ✨ Replaced simple crew execution with a **Flow-based orchestration** system
- 🎯 Added state management with `ResearchFlowState` (Pydantic model)
- 📊 Three-step flow: prepare topic → run research → save report

### 2. **Updated Crew Structure** (`crew.py`)

- 🔧 Renamed `Tomas` class to `TomasCrew` (better clarity)
- 🔍 Added `SerperDevTool` to researcher agent for web search
- 📋 Improved type hints and docstrings

### 3. **Configuration Updates**

- 📝 Updated `agents.yaml` with complete agent definitions
- ✏️ Enhanced `tasks.yaml` with better task descriptions matching documentation
- 🚀 Changed `pyproject.toml` from `type: "crew"` to `type: "flow"`

### 4. **Environment & Dependencies**

- 🌐 Created `.env.example` template for reference
- 📦 Added `crewai-tools` and `python-dotenv` to dependencies
- 🔑 Your existing `.env` is preserved with NVIDIA NIM configuration

### 5. **Documentation**

- 📖 Completely rewritten `README.md` with Flow-based instructions
- 🛠️ Added troubleshooting section
- 💡 Included examples for customization & advanced features

---

## 🚀 Running the Project

### Step 1: Install Dependencies

```bash
cd /home/pw/backend-ii/session14/tomas

# Install using uv (recommended)
uv sync

# OR using crewai CLI
crewai install
```

### Step 2: Verify Environment

Your `.env` already has:

- ✅ `MODEL=minimaxai/minimax-m2.7`
- ✅ `NVIDIA_NIM_API_KEY` configured

Optional: Add Serper API key for better web search:

```bash
# Edit .env and add (or uncomment):
SERPER_API_KEY=your-key-from-serper.dev
```

### Step 3: Run the Flow

```bash
# From project root
crewai run

# OR using uv
uv run src/tomas/main.py
```

### Step 4: Check Output

The report will be generated at:

```
output/report.md
```

View it:

```bash
cat output/report.md
```

---

## 📊 Project Structure

```
tomas/
├── src/tomas/
│   ├── main.py              ← Flow definition (prepare → research → save)
│   ├── crew.py              ← Crew with agents & tasks
│   ├── config/
│   │   ├── agents.yaml      ← Researcher + Reporting Analyst
│   │   └── tasks.yaml       ← Research + Reporting tasks
│   └── tools/
│       └── custom_tool.py
│
├── .env                     ← Your API keys (NVIDIA NIM configured)
├── .env.example            ← Template for reference
├── README.md               ← Full documentation
├── SETUP.md               ← This file
├── pyproject.toml         ← Project config (type: "flow")
└── output/                ← Generated reports go here
```

---

## 🔄 How It Works

### Flow Execution Order

1. **`prepare_topic()`** - Initialize research topic
   - Sets topic from trigger payload or default
   - Sets current year

2. **`run_research()`** - Execute the crew
   - Researcher agent searches the web using SerperDevTool
   - Reporting analyst creates structured report
   - Output saved to `output/report.md`

3. **`save_report()`** - Finalize
   - Confirmation message
   - Flow completion status

### Crew Execution

The crew runs tasks **sequentially**:

1. Researcher conducts thorough research with web search
2. Reporting analyst formats findings into a polished report

---

## ⚙️ Configuration & Customization

### Change Default Topic

Edit `src/tomas/main.py`:

```python
@start()
def prepare_topic(self, crewai_trigger_payload: dict | None = None):
    if crewai_trigger_payload:
        self.state.topic = crewai_trigger_payload.get("topic", "AI LLMs")
    else:
        self.state.topic = "YOUR_TOPIC"  # ← Change this
```

### Customize Agents

Edit `src/tomas/config/agents.yaml`:

```yaml
researcher:
  role: "Your Custom Role"
  goal: "Your custom goal"
  backstory: "Your backstory"
```

### Add More Tools

Edit `src/tomas/crew.py`:

```python
from crewai_tools import FileReadTool, ScrapeWebsiteTool

@agent
def researcher(self) -> Agent:
    return Agent(
        config=self.agents_config["researcher"],
        verbose=True,
        tools=[SerperDevTool(), ScrapeWebsiteTool()],  # Add tools here
    )
```

### Modify Tasks

Edit `src/tomas/config/tasks.yaml`:

```yaml
research_task:
  description: "Your description"
  expected_output: "Your expected format"
  agent: researcher
```

---

## 🎓 Learning Resources

### Key Concepts

1. **Flow** - Orchestrates execution order & manages state
2. **Crew** - Collection of agents working on tasks
3. **Agents** - AI workers with specific roles
4. **Tasks** - Specific jobs agents perform
5. **Tools** - Capabilities agents can use (web search, file reading, etc.)

### Documentation Links

- 📘 [CrewAI Quickstart](https://docs.crewai.com/en/quickstart)
- 🎯 [Flows Guide](https://docs.crewai.com/en/guides/flows/first-flow)
- 🤖 [Agents Documentation](https://docs.crewai.com/en/concepts/agents)
- ✅ [Tasks Documentation](https://docs.crewai.com/en/concepts/tasks)
- 🛠️ [Tools Documentation](https://docs.crewai.com/en/concepts/tools)

---

## 🐛 Troubleshooting

### Issue: "API key not found"

```bash
# Make sure .env exists and has your keys
cat .env

# Or set them as environment variables
export NVIDIA_NIM_API_KEY="your-key"
export SERPER_API_KEY="your-key"
```

### Issue: "Module not found"

```bash
# Reinstall dependencies
uv sync --refresh
# or
uv pip install -e .
```

### Issue: "CrewAI version mismatch"

```bash
# Check version
uv run python -c "import crewai; print(crewai.__version__)"

# Update if needed
uv pip install --upgrade crewai
```

### Issue: "Report not generated"

- Check `output/` directory exists
- Check agent verbose logs for errors
- Verify Serper API key if using web search

---

## ✨ Next Steps

1. ✅ Run `crewai run` to generate your first report
2. ✅ Check `output/report.md` for results
3. ✅ Customize topic & agents for your use case
4. ✅ Add custom tools or workflows
5. ✅ Deploy to CrewAI AMP when ready

---

**You're all set! Happy researching with CrewAI! 🎉**
