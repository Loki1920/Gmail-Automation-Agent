from crewai import Agent
from textwrap import dedent
from tools import EmailTools

class Agents():
    def email_filter_agent():
        return Agent(
            role='Senior Email Analyst',
            goal='Filter out non-essential emails like Marketing, newsletters and promotional content',
            backstory=dedent("""\
                As a Senior Email Analyst, you have extensive experience in email content analysis.
You are adept at distinguishing non-essential emails like Marketing, newsletters and promotional from spam, promotional, newsletters, and other
irrelevant content. Your expertise lies in identifying key patterns and markers that
signify the importance of an email. 
                             """),
            verbose=True,
            allow_delegation=False
        )
    
    def email_action_agent():
        return Agent(
            role='Email Action Specialist',
            goal='Move non-essential emails like marketing, newsletters and promotional to a specific folder based on analysis',
            backstory=dedent("""\
                As an Email Action Specialist, you are the final step in the email processing pipeline.
                You take the filtered list of non-essential emails like marketing, newsletters and promotional and execute actions on them, such as
                moving them to designated labels for organization."""),
            verbose=True,
            tools=[EmailTools.move_email], # Give the agent the move_email tool
            allow_delegation=False
        )

