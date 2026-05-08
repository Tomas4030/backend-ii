# Tomas - CrewAI Research Flow 🤖

Welcome to the Tomas Crew project, powered by [crewAI](https://crewai.com). This is a **Flow-based** research agent system with web search capabilities.

## Project Structure

```
tomas/
├── src/tomas/
│   ├── main.py                 # Flow definition & orchestration
│   ├── crew.py                 # Crew with agents & tasks
│   ├── config/
│   │   ├── agents.yaml         # Agent configurations
│   │   └── tasks.yaml          # Task definitions
│   └── tools/
│       └── custom_tool.py      # Custom tools
├── .env                        # Environment variables (COPY FROM .env.example)
├── pyproject.toml             # Project config (type: "flow")
└── output/                    # Generated reports go here
```

## Quick Start

### 1. Install Dependencies

Ensure you have Python >=3.10 <3.14 installed. Install UV if you haven't:

```bash
pip install uv
```

Install project dependencies:

```bash
cd tomas
uv sync
# or
crewai install
```

### 2. Configure Environment Variables

Copy and update `.env`:

```bash
# Use your NVIDIA NIM API key (already set)
MODEL=minimaxai/minimax-m2.7
NVIDIA_NIM_API_KEY=your-key-here

# Optional: Add Serper API key for web search
SERPER_API_KEY=your-serper-api-key-here
```

Get a free Serper API key at [serper.dev](https://serper.dev/)

### 3. Run the Flow

Execute the complete research flow:

```bash
crewai run
```

This will:

1. ✅ Prepare the research topic
2. 🔍 Run the researcher agent (with web search)
3. 📝 Run the reporting analyst
4. 💾 Save the report to `output/report.md`

### 4. View Results

Check the generated report:

```bash
cat output/report.md
```

## Understanding the Architecture

### Flow (`main.py`)

The Flow orchestrates the entire process with 3 steps:

- **`prepare_topic()`** - Sets up the research topic and year
- **`run_research()`** - Executes the crew with the researcher & reporting analyst
- **`save_report()`** - Confirms report was saved

### Crew (`crew.py`)

The crew contains 2 agents working sequentially:

**Researcher Agent**

- Role: Senior Data Researcher
- Tools: `SerperDevTool` for web search
- Task: Conduct thorough research on the topic

**Reporting Analyst**

- Role: Reporting Analyst
- Task: Create detailed reports based on research findings

### Configuration Files

**`config/agents.yaml`** - Define agent roles, goals, and backstories
**`config/tasks.yaml`** - Define task descriptions and expected outputs

## Customization

### Change the Research Topic

Edit `main.py` and modify the default topic:

```python
self.state.topic = "Your Topic Here"
```

Or pass it dynamically via trigger payload.

### Add Custom Tools

Add tools to agents in `crew.py`:

```python
from crewai_tools import FileReadTool, ScrapeWebsiteTool

@agent
def researcher(self) -> Agent:
    return Agent(
        config=self.agents_config["researcher"],
        verbose=True,
        tools=[SerperDevTool(), ScrapeWebsiteTool()],
    )
```

### Modify Agent Behavior

Edit `config/agents.yaml`:

```yaml
researcher:
  role: "Your Custom Role"
  goal: "Your custom goal"
  backstory: "Your custom backstory"
```

### Change Task Parameters

Edit `config/tasks.yaml`:

```yaml
research_task:
  description: "Your custom description"
  expected_output: "Your expected output format"
  agent: researcher
```

## Advanced Features

### Flow Visualization

Plot the flow diagram:

```python
from tomas.main import TomasFlow
flow = TomasFlow()
flow.plot()
```

### Persistent State

Add `@persist` decorator to Flow methods for SQLite-backed state:

```python
from crewai.flow import persist

@persist(table="research_flows")
def run_research(self):
    # ... state persists automatically
```

### Human Feedback Loop

Add `@human_feedback` for approval steps:

```python
from crewai.flow import human_feedback

@human_feedback()
def run_research(self):
    # ... requires human approval before proceeding
```

## Support & Documentation

- 📖 [CrewAI Docs](https://docs.crewai.com)
- 🐙 [GitHub Repository](https://github.com/crewAIInc/crewAI)
- 💬 [Discord Community](https://discord.com/invite/X4JWnZnxPb)
- 📝 [Flow Guide](https://docs.crewai.com/en/guides/flows/first-flow)

## Troubleshooting

### API Key Issues

```bash
# Check if .env is loaded
echo $OPENAI_API_KEY
```

### Module Import Errors

```bash
# Reinstall dependencies
uv sync --refresh
```

### Report Not Generated

Check `output/` folder permissions and ensure agents ran successfully (check verbose logs).

---

**Let's create wonders together with the power and simplicity of crewAI!** ✨
