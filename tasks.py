from crewai import Task
from textwrap import dedent


class Tasks():
    def filter_email_tasks(agent,emails):
        return Task(
        description=dedent(f"""\
            Analyze a batch of emails and filter out
non-essential ones such as marketing , newsletters, promotional content and notifications.

Use your expertise in email content analysis to distinguish
non-essential emails like marketing , promotional , newsletters email from the rest, pay attention to the sender and avoid invalid emails.

Make sure to filter for the messages actually directed at the user .

EMAILS
-------
{emails}

Your final answer MUST be the relevant thread_ids and the sender, use bullet points.
"""),
agent=agent,
expected_output="A bullet-point list containing only the relevant thread_ids and sender of important emails."

    )

    def move_email_task( agent, context, label_name):
        return Task(
            description=dedent(f"""\
                For each non-essential email like marketing , promotional , newsletters identified in the context, use your tool to move it 
                to the '{label_name}' label in Gmail.

                The context contains a list of non-essential email like marketing , promotional , newsletters , each with a unique 'id'.
                
                Context:
                {context}
                
                Iterate through each email in the context and call the move tool with the
                correct 'id' and the destination label '{label_name}'.
            """),
            agent=agent,
            context=context, # The output of the filter_email_task
            expected_output=f"A confirmation message for each email moved to the '{label_name}' label."
        )