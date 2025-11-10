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
