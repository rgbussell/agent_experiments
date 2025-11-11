# agent_experiments
## Projects with LLM-based Agents

### Gemini Agents

#### Launch the ADK Web Server
- Provides a localhost:8000 UI by default
- Launch the command at top of the agents directories
```bash
adk web
```

- Starts a local web server
- Working directory should be above the agents directory
- Each directory in the current working directory appears as an "agent" in the browser

#### Agent Filesystem Setup
```
cwd_for_adk_web/
├── agent1/
│   ├── .env (API keys)
│   └── agent.py (agent definition)
└── agent2/
        ├── .env
        └── agent.py
```

### Function Calls

- Prompt the caller agent with the function name
- Include type hints to define the function (may help the caller)
- Provide the function objects as a tool
- If the tool is an agent, provide it as `AgentTool(agent=agent_object)`

### ADK Web Interface

The web interface provides a UI for prompting the root agent and displays:

- **Trace**: Invocations and calls
- **Events List**: Graphical architecture of agents involved, details of calls and actions
- **States**
- **Artifacts**
- **Session ID**
- **Eval**