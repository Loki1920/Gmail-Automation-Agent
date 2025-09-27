from agents import Agents 
from tasks import Tasks
from gmail_service import fetch_mails
from crewai import Crew, Process


# --- CONFIGURATION ---
# The name of the label you want to move important emails to.

DESTINATION_LABEL = "From Marketing Lists"

# --- Initialize Agents and Tasks ---
agents = Agents()
tasks = Tasks()

# create filter agent 
filter_agent = Agents.email_filter_agent()

# action agent
action_agent = Agents.email_action_agent()

# create filter task

emails = fetch_mails()
filter_task = Tasks.filter_email_tasks(filter_agent,emails)

# The move_task will use the output of the filter_task as its context
move_task = Tasks.move_email_task(
    agent=action_agent, 
    context=[filter_task], 
    label_name=DESTINATION_LABEL
)

# assemble crew 
crew = Crew(
    agents=[filter_agent,action_agent],
    tasks =[filter_task, move_task],
    process=Process.sequential
)

# start process 
# --- Start the Process ---
if emails:
    result = crew.kickoff()
    print("\n\n########################")
    print("## Crew Execution Result:")
    print("########################")
    print(result)
else:
    print("No emails to process.")