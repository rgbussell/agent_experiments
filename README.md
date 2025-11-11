# agent_experiments
Some basic experiments buillding LLM based agents

# Gemmini agents
Launch the adk webserver
>> adk web
* This starts a local web server
* Working directory should be above the agents directory
* Each directory in the cwd appears as an "agent" lists in the browser

Agent filesystem setup
cwd_for_adk_web
|->agent1
        |->.env (API keys)
        |->agent.py (agent definition)
|->agent2
        |->.env
        |->agent.py


# Function calls
Prompt the caller agent with the function name.
Include type hints to define the funtion (maybe helps the caller)
Provide the function objects as a tool
If the tool is an agent, provide it as AgentTool(agent=agent_object)

# adk web
The web interface provides a UI for prompting the root agent
The web interface displays
* a trace with invocations and calls
* and events list which lists with graphical architecture of the 
    agents involved in the event and details of each of the
    calls and actions
* states
* artifacts
* session id
* Eval